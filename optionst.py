# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Command line options."""

import logging
import platform

from sourcet import Sources
import symbolt
from symbolt import Tags
import filet
from filet import File

import version as viewer_version

def goto(parser):
    'Define --goto command line option.'

    parser.add_argument(
        '--goto',
        help="""
        The goto binary.
        """
    )
    return parser

def srcdir(parser):
    'Define --srcdir command line option.'

    parser.add_argument(
        '--srcdir',
        help="""
        The source directory.  The root of the source tree.
        """
    )
    return parser

def wkdir(parser):
    'Define --wkdir command line option.'

    parser.add_argument(
        '--wkdir',
        help="""
        The working directory in source locations in the goto binary
        (and omitted when source locations are printed in textual form).
        This is usually the directory in which goto-cc was invoked to
        build the goto binary.
        """
    )
    return parser

def reportdir(parser):
    'Define --reportdir command line option.'

    parser.add_argument(
        '--reportdir',
        default='report',
        help="""
        The report directory.  Write the final report to this directory.
        (Default: %(default)s)
        """
    )
    return parser

def result(parser):
    'Define --result command line option.'

    parser.add_argument(
        '--result',
        metavar='FILE',
        default=['result.xml'],
        nargs='+',
        help="""
        CBMC property checking results.
        A text, xml, or json file containing the output of 'cbmc'.
        (Default: %(default)s)
        """
    )
    return parser

def coverage(parser):
    'Define --coverage command line option.'

    parser.add_argument(
        '--coverage',
        metavar='FILE',
        default=['coverage.xml'],
        nargs='+',
        help="""
        CBMC coverage checking results.
        An xml or json file containing the output of
        'cbmc --cover locations'. (Default: %(default)s)
        """
    )
    return parser

def property(parser):
    'Define --property command line option.'

    # pylint: disable=redefined-builtin

    parser.add_argument(
        '--property',
        metavar='FILE',
        default=['property.xml'],
        nargs='+',
        help="""
        CBMC properties checked during property checking.
        An xml or json file containing the output of
        'cbmc --show-properties'.
        (Default: %(default)s)
        """
    )
    return parser

def exclude(parser):
    'Define --exclude command line option.'

    parser.add_argument(
        '--exclude',
        help="""
        Paths relative to SRCDIR to exclude from the list of source files.
        A Python regular expression matched against the result
        of os.path.normpath().  The match is case insensitive.
        """
    )
    return parser

def extensions(parser):
    'Define --extensions command line option.'

    parser.add_argument(
        '--extensions',
        metavar='REGEXP',
        default=r'^\.(c|h|inl)$',
        help="""
        File extensions of files to include in the list of source files.
        A Python regular expression matched against the result of
        os.path.splitext().  The match is case insensitive.
        (Default: %(default)s)
        """
    )
    return parser

def source_method(parser):
    'Define --source-method command line option.'

    choices = []
    if platform.system() != 'Windows':
        choices.append('find')
    choices.extend(['walk', 'make', 'goto'])

    parser.add_argument(
        '--source-method',
        metavar='MHD',
        choices=choices,
        help="""
        The method to use to list source files under SRCDIR.  Methods
        available are [%(choices)s]: Use the Linux 'find' command, use
        the Python 'walk' method, use the 'make' command to build
        the goto binary with the preprocessor, or use the symbol table in
        the goto binary.  The default method is 'goto' if
        SRCDIR and WKDIR and GOTO are specified, 'make' if SRCDIR and WKDIR
        are specified, 'walk' on Windows, and 'find' otherwise.
        """
    )
    return parser

def tags_method(parser):
    'Define --tags_method command line option.'

    parser.add_argument(
        '--tags-method',
        metavar='TAGS',
        choices=['ctags', 'etags'],
        help="""
        ctags: exuberant ctags
        etags: emacs tags
        """
    )
    return parser

def config(parser):
    'Define --config command line option.'

    parser.add_argument(
        '--config',
        metavar='JSON',
        default="cbmc-viewer.json",
        help="""
        JSON configuration file. (Default: '%(default)s')
        """
    )
    return parser

################################################################
# Load data from the make-* commands

def viewer_reachable(parser):
    "Load make-reachable data"

    parser.add_argument(
        '--viewer-reachable',
        metavar='JSON',
        nargs='+',
        help='Load reachable functions from the JSON output of make-reachable.'
        ' If multiple files are given, merge multiple data sets into one.'
    )

def viewer_coverage(parser):
    "Load make-coverage data"

    parser.add_argument(
        '--viewer-coverage',
        metavar='JSON',
        nargs='+',
        help='Load coverage data from the JSON output of make-coverage.'
        ' If multiple files are given, merge multiple data sets into one.'
    )

def viewer_loop(parser):
    "Load make-loop data"

    parser.add_argument(
        '--viewer-loop',
        metavar='JSON',
        nargs='+',
        help='Load loops from the JSON output of make-loop.'
        ' If multiple files are given, merge multiple data sets into one.'
    )

def viewer_property(parser):
    "Load make-property data"

    parser.add_argument(
        '--viewer-property',
        metavar='JSON',
        nargs='+',
        help='Load properties from the JSON output of make-property.'
        ' If multiple files are given, merge multiple data sets into one.'
    )

def viewer_result(parser):
    "Load make-result data"


    parser.add_argument(
        '--viewer-result',
        metavar='JSON',
        nargs='+',
        help='Load results from the JSON output of make-result.'
        ' If multiple files are given, merge multiple data sets into one.'
    )

def viewer_source(parser):
    "Load make-source data"

    parser.add_argument(
        '--viewer-source',
        metavar='JSON',
        nargs='+',
        help='Load sources from the JSON output of make-source.'
        ' If multiple files are given, merge multiple data sets into one.'
    )
def viewer_symbol(parser):
    "Load make-symbol data"

    parser.add_argument(
        '--viewer-symbol',
        metavar='JSON',
        nargs='+',
        help='Load symbols from the JSON output of make-symbol.'
        ' If multiple files are given, merge multiple data sets into one.'
    )

def viewer_trace(parser):
    "Load make-trace data"

    parser.add_argument(
        '--viewer-trace',
        metavar='JSON',
        nargs='+',
        help='Load traces from the JSON output of make-trace.'
        ' If multiple files are given, merge multiple data sets into one.'
    )
    return parser

################################################################
# Set logging levels

def log(parser):
    'Define --verbose and --debug command line options.'

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Verbose output.'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Debugging output.'
    )
    return parser

def version(parser):
    'Define --version command line option.'

    parser.add_argument(
        '--version',
        action='version',
        version=viewer_version.version(),
        help="""Display version number and exit."""
    )
    return parser

################################################################
# Set default values for arguments

def default_logging(args):
    'Set default logging configuration.'

    # Only the first invocation of basicConfig configures the root logger
    if getattr(args, 'debug', False):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s: %(message)s')
    if getattr(args, 'verbose', False):
        logging.basicConfig(level=logging.INFO,
                            format='%(levelname)s: %(message)s')
    logging.basicConfig(format='%(levelname)s: %(message)s')

    return args

def default_source_method(args):
    'Set default source method.'

    # Set source_method to an enum
    if hasattr(args, 'source_method'):

        # Set source method to its enum value or None
        args.source_method = {
            'find': Sources.FIND,
            'walk': Sources.WALK,
            'make': Sources.MAKE,
            'goto': Sources.GOTO,
            None: None
        }[args.source_method]

        # Set source method to a reasonable default value
        if args.source_method is None:
            if getattr(args, 'srcdir') is not None:
                if getattr(args, 'wkdir') is not None:
                    if getattr(args, 'goto') is not None:
                        args.source_method = Sources.GOTO
                    else:
                        args.source_method = Sources.MAKE
                elif platform.system() == 'Windows':
                    args.source_method = Sources.WALK
                else:
                    args.source_method = Sources.FIND

        # Confirm existence of command line options needed by source method
        if args.source_method == Sources.GOTO:
            if (not hasattr(args, 'srcdir') or
                    not hasattr(args, 'wkdir') or
                    not hasattr(args, 'goto')):
                raise UserWarning('Options --srcdir, --wkdir, and --goto '
                                  'required by source method goto.')

        if args.source_method == Sources.FIND:
            if not hasattr(args, 'srcdir'):
                raise UserWarning('Option --srcdir required '
                                  'by source method find.')

        if args.source_method == Sources.WALK:
            if not hasattr(args, 'srcdir'):
                raise UserWarning('Option --srcdir required '
                                  'by source method walk.')

        if args.source_method == Sources.MAKE:
            if not hasattr(args, 'srcdir') or not hasattr(args, 'wkdir'):
                raise UserWarning('Options --srcdir and --wkdir required '
                                  'by source method make.')

    return args

def default_tags_method(args):
    'Set default tags method.'

    # Set tags_method to an enum
    if hasattr(args, 'tags_method'):
        args.tags_method = {
            'ctags': Tags.CTAGS,
            'etags': Tags.ETAGS,
            None: None
        }[args.tags_method]

        if args.tags_method is None:
            if symbolt.have_ctags():
                args.tags_method = Tags.CTAGS
            elif symbolt.have_etags():
                args.tags_method = Tags.ETAGS
            else:
                # No ctags or etags means symbols will not be linked to code
                logging.warning("Install ctags for better results.")

        if args.tags_method == Tags.ETAGS:
            # Scanning a large source tree for symbols is slow.
            # etags can be faster than ctags, but ctags is a more
            # reliable parser of oddly-formatted code
            logging.warning("Consider installing ctags for better results.")

    return args

def warn_against_using_text_for_cbmc_output(args):
    'Recommend the use of xml or json input instead of text.'

    for attr in ['result', 'coverage', 'property']:
        filenames = getattr(args, attr, None)
        if (filenames and
                any([filet.filetype(name) == File.TEXT for name in filenames])):
            logging.warning("Use xml or json instead of text for "
                            "better results: %s", filenames)

def defaults(args):
    'Set default values based on command line arguments.'

    args = default_logging(args)
    args = default_source_method(args)
    args = default_tags_method(args)
    warn_against_using_text_for_cbmc_output(args)
    return args

################################################################