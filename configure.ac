#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.61)
AC_INIT([jconfpy], m4_esyscmd([ tr -d '\n' < version ]))

AC_CONFIG_SRCDIR([src/jsonPy.pym])
AC_CONFIG_SRCDIR([src/jsonPy.c])
AC_CONFIG_SRCDIR([include/jsonPy.h])

AC_CONFIG_HEADER([include/config.h])

LT_INIT
AM_INIT_AUTOMAKE
AM_MAINTAINER_MODE([disable])
AM_PATH_PYTHON([2.7])

AC_CONFIG_MACRO_DIR([m4])

AC_CONFIG_FILES([Makefile
		src/Makefile
		test/Makefile])

# Checks for programs.
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_LN_S

# Checks for header files.
AC_HEADER_STDC

# End To check

# Checks for typedefs, structures, and compiler characteristics.
AC_HEADER_STDBOOL
AC_C_CONST
#AC_TYPE_SIZE_T

# Libs list autmatically generated from dependecy script
# AC_CHECK_LIB([crypto],[BIO_ctrl],[],[AC_MSG_FAILURE([could not find lib crypto])])

AC_CANONICAL_HOST
case $host_os in
  darwin* )
		AM_CONDITIONAL(OSX, true)
		AM_CONDITIONAL(LINUX, false)
		AM_CONDITIONAL(UNSUPPORTED, false)
        ;;
  linux*)
		AM_CONDITIONAL(LINUX, true)
		AM_CONDITIONAL(OSX, false)
		AM_CONDITIONAL(UNSUPPORTED, false)
        ;;
    *)
		AM_CONDITIONAL(UNSUPPORTED, true)
		AM_CONDITIONAL(LINUX, false)
		AM_CONDITIONAL(OSX, false)
            	#AC_MSG_ERROR([Your platform is not currently supported])
        ;;
esac


AC_OUTPUT
