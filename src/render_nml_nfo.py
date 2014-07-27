"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

print "[PYTHON] render pnml"

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import global_constants
import os
currentdir = os.curdir
src_path = os.path.join(currentdir, 'src')
from multiprocessing import Pool
import subprocess
import StringIO

import global_constants as global_constants
import utils as utils
import firs
import cargos
from cargos import registered_cargos
import industries
from industries import registered_industries

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(src_path, 'templates'), format='text')
industry_templates = PageTemplateLoader(os.path.join(src_path, 'industries'), format='text')

generated_pnml_path = os.path.join(firs.generated_files_path, 'pnml')
if not os.path.exists(generated_pnml_path):
    os.mkdir(generated_pnml_path)
generated_nml_path = os.path.join(firs.generated_files_path, 'nml')
if not os.path.exists(generated_nml_path):
    os.mkdir(generated_nml_path)
generated_nfo_path = os.path.join(firs.generated_files_path, 'nfo')
if not os.path.exists(generated_nfo_path):
    os.mkdir(generated_nfo_path)

header_pnml = StringIO.StringIO()
dummy_pnml = StringIO.StringIO()
grf_nfo = codecs.open(os.path.join(firs.generated_files_path, 'firs.nfo'),'w','utf8')


def check_industry_needs_compiling(industry):
    test_industry_flag = repo_vars.get('test_industry', None)
    if test_industry_flag is None or test_industry_flag == '' or test_industry_flag == 'None':
        return True
    elif test_industry_flag == industry.id:
        return True
    else:
        return False


def render_nml(filename):
    print "Rendering nml for " + filename
    gcc_call_args = ['gcc',
                      '-D',
                      'REPO_REVISION='+str(repo_vars['repo_version']),
                      '-C',
                      '-E',
                      '-nostdinc',
                      '-x',
                      'c-header',
                      'generated/pnml/' + filename + '.pnml',
                      '-o',
                      'generated/nml/' + filename + '.nml']
    subprocess.call(gcc_call_args)


def render_nfo(filename):
    print "Rendering nfo for " + filename
    nmlc_call_args = ['nmlc',
                      '--lang-dir=lang',
                      #'--quiet',
                      '--nfo',
                      'generated/nfo/' + filename + '.nfo',
                      'generated/nml/' + filename + '.nml']
    subprocess.call(nmlc_call_args)


def render_cargo_pnml(cargo):
    print "Rendering pnml for " + cargo.id
    pnml_file = codecs.open(os.path.join(generated_pnml_path, cargo.id + '.pnml'), 'w','utf8')
    pnml_file.write(cargo.render_pnml())
    pnml_file.close()


def render_industry_pnml(industry):
    print "Rendering pnml for " + industry.id
    if check_industry_needs_compiling(industry):
        # save the results of templating
        pnml_file = codecs.open(os.path.join(generated_pnml_path, industry.id + '.pnml'), 'w','utf8')
        #pnml_file.write(header_pnml.getvalue())
        pnml_file.write(dummy_pnml.getvalue())
        pnml_file.write(industry.render_pnml())
        pnml_file.close()


def render_dispatcher(items, renderer):
    if repo_vars.get('no_mp', None) == 'True':
        for item in items:
            renderer(item)
    else:
        pool = Pool(processes=16) # 16 is an arbitrary amount that appears to be fast without blocking the system
        pool.map(renderer, items)
        pool.close()
        pool.join()


def link_nfo(item, dep_path, split=None):
    #dep_timestamps_new[dep_path] = os.stat(dep_path).st_mtime
    item_nfo = codecs.open(os.path.join('generated', 'nfo', item + '.nfo'),'r','utf8').read()
    if split is not None:
        # fragile split on some specific nfo, may break; assumes a right-split only
        if split in item_nfo:
            print 'split found ' + item
            item_nfo = item_nfo.split(split)[1]
        else:
            print 'split not found ' + item
    grf_nfo.write(item_nfo)


def main():
    if repo_vars.get('no_mp', None) == 'True':
        utils.echo_message('Multiprocessing disabled: (NO_MP=True)')

    print "Rendering Header"
    header_items = ['header', 'parameters', 'checks', 'disable_default_cargos', 'cargo_table']
    for header_item in header_items:
        template = templates[header_item + '.pypnml']
        header_pnml.write(utils.unescape_chameleon_output(template(registered_industries=registered_industries,
                                        registered_cargos=registered_cargos, global_constants=global_constants,
                                        utils=utils, sys=sys, generated_pnml_path=generated_pnml_path)))
    render_dispatcher(registered_cargos, renderer=render_cargo_pnml)
    for cargo in registered_cargos:
        header_pnml.write(codecs.open(os.path.join(generated_pnml_path, cargo.id + '.pnml'), 'r','utf8').read())

    header_pnml_file = codecs.open(os.path.join(generated_pnml_path, 'header.pnml'), 'w','utf8')
    header_pnml_file.write(header_pnml.getvalue())
    header_pnml_file.close()

    template = templates['dummy.pypnml']
    dummy_pnml.write(utils.unescape_chameleon_output(template(registered_industries=registered_industries,
                            registered_cargos=registered_cargos, global_constants=global_constants,
                            utils=utils, sys=sys, generated_pnml_path=generated_pnml_path)))
    dummy_pnml_file = codecs.open(os.path.join(generated_pnml_path, 'dummy.pnml'), 'w','utf8')
    dummy_pnml_file.write(dummy_pnml.getvalue()) # only writing this so it's easy to check output
    dummy_pnml_file.close()

    render_dispatcher(industries.registered_industries, renderer=render_industry_pnml)

    print "Rendering nml from pnml"
    # render nml from pnml
    render_dispatcher(['header'], renderer=render_nml)
    #render_dispatcher([cargo.id for cargo in registered_cargos], renderer=render_nml)
    render_dispatcher([industry.id for industry in industries.registered_industries], renderer=render_nml)

    print "Rendering nfo from nml"
    # render nfo from nml

    render_dispatcher(['header'], renderer=render_nfo)
    """
    render_dispatcher([cargo.id for cargo in registered_cargos], renderer=render_nfo)
    """
    render_dispatcher([industry.id for industry in industries.registered_industries], renderer=render_nfo)

    # linker
    print "Linking nfo"
    dummy_split = "// DUMMY_CALLBACK_CARGO;"

    link_nfo('header', header_item, split=None)
    """
    for cargo in registered_cargos:
        link_nfo(cargo.id, cargo.id, split=dummy_split)
    """
    for industry in industries.registered_industries:
        if check_industry_needs_compiling(industry):
            link_nfo(industry.id, industry.id, split=dummy_split)
    grf_nfo.close()

    # some warnings suppressed when we call nforenum; assume nmlc has done the right thing and nforenum is wrong
    nforenum_call_args = ['nforenum',
                      '--silent',
                      '--warning-disable=62,80,84,90,97,99,100,109,111,118,141,144,147,162,164,170,172,188,202,204,209',
                      'generated/firs.nfo']
    subprocess.call(nforenum_call_args)

    """
    dep_timestamps_file = codecs.open(dep_timestamps_path, 'w', 'utf8')
    dep_timestamps_file.write(json.dumps(dep_timestamps_new))
    dep_timestamps_file.close()
    """

if __name__ == '__main__':
    main()
