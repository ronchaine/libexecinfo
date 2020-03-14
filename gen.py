#!/usr/local/bin/python
#
# Copyright (c) 2003 Maxim Sobolev <sobomax@FreeBSD.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#
# $Id: gen.py,v 1.1 2003/08/10 14:47:54 sobomax Exp $

PROLOGUE = '#include <stddef.h>\n\n#include "stacktraverse.h"\n\nvoid *\nget%saddr(int level)\n{\n\n    switch(level) {'
BODY = '    case %d: return __builtin_%s_address(%d);'
EPILOGUE = '    default: return NULL;\n    }\n}'

MAXDEPTH = 128

def gen(name, maxnum):
	print PROLOGUE % name
	for i in range(0, maxnum):
		print BODY % (i, name, i + 1)
	print EPILOGUE

gen("return", MAXDEPTH)
print ''
gen("frame", MAXDEPTH)
