# (c) Copyright 2023 by Coinkite Inc. This file is covered by license found in COPYING-CC.
#
# Binary for Q1 GPU co-processor
# 
# see misc/gpu for source
# 
VERSION = '1.1.1'

LENGTH = const(3496)  # bytes

BINARY = (b'\x00\x18\x00 \t\x01\x00\x08\x19\t\x00\x08\x1b\t\x00\x08\x00\x00\x00\x00'
 b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
 b'\x00\x00\x00\x00\x00\x00\x00\x00\x1d\t\x00\x08\x00\x00\x00\x00'
 b'\x00\x00\x00\x00\x1f\t\x00\x08!\t\x00\x08U\x01\x00\x08\x00\x00\x00\x00'
 b'U\x01\x00\x08U\x01\x00\x08U\x01\x00\x08U\x01\x00\x08U\x01\x00\x08'
 b'U\x01\x00\x08\x00\x00\x00\x00U\x01\x00\x08U\x01\x00\x08U\x01\x00\x08'
 b'U\x01\x00\x08U\x01\x00\x08U\x01\x00\x08\x00\x00\x00\x00U\x01\x00\x08'
 b'\x00\x00\x00\x00\x00\x00\x00\x00U\x01\x00\x08\x00\x00\x00\x00U\x01\x00\x08'
 b'U\x01\x00\x08U\x01\x00\x08\x00\x00\x00\x00U\x01\x00\x08\x00\x00\x00\x00'
 b'U\x01\x00\x08U\x01\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
 b'\x10\xb5\x06L#x\x00+\x07\xd1\x05K\x00+\x02\xd0\x04H\x00\xe0\x00\xbf\x01#'
 b'#p\x10\xbd\x08\x00\x00 \x00\x00\x00\x00\x9c\r\x00\x08\x04K\x10\xb5'
 b'\x00+\x03\xd0\x03I\x04H\x00\xe0\x00\xbf\x10\xbd\xc0F\x00\x00\x00\x00'
 b'\x0c\x00\x00 \x9c\r\x00\x08\x0cH\x85F\x00\xf0\x96\xf9\x00!\x03\xe0\nK[X'
 b'CP\x041\tH\nKB\x18\x9aB\xf6\xd3\tJ\x02\xe0\x00#\x13`\x042\x07K\x9aB'
 b'\xf9\xd3\x00\xf0\xc7\xf9\xfe\xe7\x00\x18\x00 \x00\x00\x00 \x00\x00\x00 '
 b'\x08\x00\x00 \x08\x00\x00 D\x00\x00 \xfe\xe7\x00\x00\x00\xb5\x89\xb0'
 b'\x14"\x00!\x03\xa8\x00\xf0\xc7\xfd\x01 \tJQk\x01CQcSk\x02\xa9\x03@\x01\x93'
 b'\x01\x9b?#\x9f0\x02\x93\xc0\x05=;\x04\x93\x00\xf0\xcc\xfb\t\xb0\x00\xbd\xc0F'
 b'\x00\x10\x02@\x10\xb5\x02$ K!IZm\x88\xb0\n@ZeZk\x00!"CZc[k\x0c"#@\x00\x93'
 b'\x03\xa8\x00\x9b\x00\xf0\x9c\xfd\xc0#\x01\x93\xbf;\x04\x93\x01\xa9\x053'
 b'\x16H\x06\x93\x02\x94\x00\xf0\xa8\xfb\x1c"\x00!\x01\xa8\x00\xf0\x8c\xfd'
 b'\x12K\x13L\x02\x93\xca# \x00\x01\xa9\x05\x93\x00\xf0+\xfd\x80#bh\x9b\x04'
 b'\x13Cc`\xe3h\rJ\x13@\xe3`\xe3h\x0cJ\x13@\xe3`#h\x0bJ\x13@#`#h\nJ\x13@#`'
 b'\x08\xb0\x10\xbd\x00\x10\x02@\xff\xcf\xff\xff\x00\x04\x00P\x13\x04\x10\x00'
 b'\x00T\x00@\x01\xf8\xff\xff\xff\x7f\xff\xff\xff\xff\xf7\xff\xff\xff\xfd\xff'
 b'\x80#\x03J[\x02\x11h\x0bC\x13`pG\xc0F\x00 \x02@\x08#\xf7\xb5jLkJ\xa1i\x19B'
 b'\x10\xd0\xe1i\x0bC\x80!\xe3a\xa3iI\x02\x0b@\x19\x00H\x1e\x81A\x11p\x00+$\xd1'
 b'cI\x0bpcI\x0bp\x13x\xa1i\x01\x93`K\x1fx`K\x1dx #\x19B4\xd0\xe2i\x13C'
 b'\xe3a\x01\x9b\x00+.\xd1[N3pc/[\xd0\x10\xd8a/\x00\xd1r\xe0b/L\xd0V/\x15\xd0'
 b'VKWJ\x1a`\x08#C\xe0#hUI\x0b@#`\xd9\xe7t/\x00\xd1l\xe0PKv/3\xd0p/\xed\xd1PJ5p'
 b'\x1a`\x08\xe0\x00-h\xd1NHJK\x18`\x00\xf0\x07\xfd\x0100p\x01#\xa2i\x13C'
 b'\xa3a\x00"\x04#\x11\x00\x9cF\x01 fF\xa3i3BY\xd1\x00)\x01\xd0<K\x1fp'
 b"\x00*\x01\xd0;K\x1dp\xff'\x00%\x02&\xbcF9H:I\x03x\nh\x01\x9f\x00/X\xd1\x00-"
 b'\x01\xd0\x03p\n`\xf7\xbd\x00-:\xd18J\x1a`\x06#3p\xd3\xe7\x00-3\xd1\xff\xf7'
 b's\xff5K.J\x13`\x03#\xf4\xe7\x04-*\xd1.I2J\x0bxSpKx\x93p\x8bxXBXA^\x1e'
 b'\xb3A\xc0\x00\x9b\x00\x03C\xc8xA\x1e\x88A=!\x00\x01\x03C\x10x\x88C\x03C\x13p'
 b'\xaf\xe7\x00-\x0f\xd1\r"$I\x0bx\x93C\x1a\x00\x01#\x13C\x0bp\xa4\xe7'
 b'\x00-\x04\xd1\x02#\x1fJ\x11x\x0bC\xeb\xe7\x16K\x1dJ\x1a`\t#\xc2\xe7'
 b'cj\xdb\xb2\x00/\x07\xd0\x07-\x9b\xd8\x13Nj\x1csU\xd5\xb2\x02\x00\x95\xe7'
 b'\x1f\x00\x01\x00\x92\xe7gF\xa7b\xa3\xe7\xa7i7B\xa3\xd0\x00+\xf7\xd0\x15x'
 b'\x01;\xa5b\x012\x01\x9d\xdb\xb2\x97\xe7\x00T\x00@.\x00\x00 -\x00\x00 '
 b'$\x00\x00 4\x00\x00 0\x00\x00 5\r\x00\x08\xff\xff\xfe\xff%\x00\x00 '
 b'p\r\x00\x08,\r\x00\x082\r\x00\x08<\x00\x00 >\r\x00\x08\x80"\x1aK'
 b'\x12\x05\x9a`\x80"\x19KR\x00\x19h\nC\x1a`\x80"\xd2\x00\x19h\x11B\xfc\xd0Zh'
 b'\x14I\x11@\x80"\xd2\x01\nCZ`\x1ah\x12I\x11@\x80"R\x01\nC\x1a`\x9ah\x0fI\n@'
 b'\x07!\x9a`\x9ah\x8aC\x9a`8"\x99h\x08\x00\x10@\x11B\xfa\xd1\x9ah\tI\n@'
 b'\x9a`\tK\tJZ`\x05"\x98`\x1a`pG\x00\xed\x00\xe0\x00\x10\x02@\xff\x80\xff\xff'
 b'\xff\xc7\xff\xff\xff\xf0\xff\xff\xff\x8f\xff\xff\x10\xe0\x00\xe0'
 b'\xdf.\x00\x00\x18Ks\xb5\x19l\x18H\xa0$\x01C\x19d\x81!\x01&\x1alI\x05\x02@'
 b'\x01\x92\x01\x9a\xdak\xe4\x05\nC\xdac\xdbk\x0b@\x00\x93\x00\x9b\xff\xf70\xfe'
 b'\x00\xf0\xbc\xf8\xff\xf7J\xfe\x0cJ\rI\x13h\x0b@\x13`\xff\xf7\xa3\xfe#i'
 b'3B\xfa\xd1 %#i+B\xf6\xd0\x00\xf0\x92\xf9#i+B\xf1\xd0\xff\xf7\x95\xfe\xf9\xe7'
 b'\x00\x10\x02@\x01\x10\x00\x00\x00 \x02@\xff\xff\xfe\xff\xa0#\x10"'
 b'\x08!\xdb\x05\x10\xb5\x9aa\x99b\x9ab\xc0#[\x01\x1c\x00\x08J\x91h\x19@'
 b'\xa1B\xfb\xd0\x10s\x91h\x19B\xfc\xd1\xa0#\x10"\xdb\x05\x9aa\x08:\x9aa'
 b'\x10\xbd\xc0F\x000\x01@\xa0#0\xb5\x10"\x08$\xdb\x05\x9aa\x9ca\x9ab\xc0"\x00#'
 b'\tLR\x01\x98B\x07\xdc\xa3h\x13B\xfc\xd1\xa0#\x10"\xdb\x05\x9aa0\xbd'
 b'\xa5h\x15@\x95B\xfb\xd0\xcd\\\x013%s\xed\xe7\x000\x01@s\xb5\x0e\x00'
 b'\x1d\x00\x01:\x83\xb2\x9a\x18\x01\xac\x92\xb2\x1b\n#p`p\x13\n* \xa3p'
 b'\xe2p\xff\xf7\xb1\xff!\x00\x04 \xff\xf7\xcb\xff\x01=\xb2\xb2U\x19'
 b'\xad\xb2\x12\n"p+ *\n\xa2pfp\xe5p\xff\xf7\xa0\xff!\x00\x04 \xff\xf7\xba\xff'
 b', \xff\xf7\x99\xffs\xbd\xa0#p\xb5\x10"\x08$\xdb\x05\x9aa\x9ca\x9ab'
 b'\xc0#\xce\xb2\xe1@\x00$\x0bJ[\x01\xa0B\x07\xdc\x91h\x19B\xfc\xd1\xa0#'
 b'\x10"\xdb\x05\x9aap\xbd\x95h\x1d@\x9dB\xfb\xd0\x16s\x95h\x1d@\x9dB'
 b'\xfb\xd0\x11s\x014\xe9\xe7\x000\x01@p\xb5\x1c\x00\x04\xab\x1e\x88'
 b'#\x00\x15\x00\xff\xf7\xa8\xff \x001\x00hC\xff\xf7\xcd\xffp\xbd'
 b'\x10\xb5\x8a\xb0\x1c"\x00!\x03\xa8\x00\xf09\xfb\xc0#\x1b\x02\x00\x93'
 b'\x82#[\x00\x01\x93\xe0#\xdb\x00\x02\x93\x80#\tLiF\x9b\x00 \x00\x05\x93'
 b'\x00\xf0\x92\xfa@#"h\x13C#`\x01#\x04J\x11x\x0bC\x13p\n\xb0\x10\xbd\xc0F'
 b'\x000\x01@<\x00\x00 \xf7\xb5\x16\x00\x08\xaa\x12x\x94F!(0\xdc\t).\xdc\x16%'
 b'\t"MCPC)\x00bF\x12$\xc7\x1d\x0f1\x00*\x00\xd1\t<\x00+.\xd1\x00.'
 b'\x1f\xd0\x1e\x00\x01#"\x008\x00\x00\x96\xff\xf7\xaa\xff)\x00\x01#"\x008\x00'
 b'$1\x105\x00\x96\xff\xf7\xa1\xff\x14#\x01")\x008\x00\x00\x96\xff\xf7\x9a\xff'
 b'\x14#\x01")\x008\x19\x018\x00\x96\xff\xf7\x92\xff\xf7\xbd\x08K"\x00\x00\x93'
 b'8\x00\x16#\xf6\xe7)\x00\x14#\xa2\x1e\x101\x080\x00\x96\xef\xe7\x00.\xf6\xd0'
 b'\x00N\xcf\xe7\xfd`\x00\x00\xf7\xb5\x1dKR!\x00\xaf\x9dDnF\x00"\x06$\x1aH\xff1'
 b'\x13\x00#@]BkA\x18M[B\x03@[\x19U\x00\x012sS\x8aB\xf2\xd1\x03#\xa0"\xed!'
 b'\x00 [BR\x00\xff\xf7\x0f\xff\x03$\x10M\xa0 +h\x80\x00{`\x0f#zh\x01<'
 b'\x99\x1aI\x00q\x18\xff\xf7\xe1\xfe\x00,\xf0\xd1{h\tJ\x013\x13@\x04\xd5'
 b'\x10"\x01;RB\x13C\x013\xbdF+`\xf7\xbdX\xfd\xff\xff\x03\x9f\xff\xff'
 b'\xfd`\x00\x00@\x00\x00 \x0f\x00\x00\x80\xf8\xb5\x14K\x00\xaf\x9dDlF\x80 '
 b'"\x00\x00!\x06\x00\x11K[\\\x03@\x1d\x00kBkA[B\x13\x80@\x08\x14\xd1\x011'
 b'()\x10\xd1\xa0"x#\xa0&R\x00\xff\xf7\xcc\xfex%\xb6\x00!\x000\x00\x01=\xff\xf7'
 b'\xa5\xfe\x00-\xf8\xd1\xbdF\xf8\xbd0\x00\x022\xde\xe7\x80\xfd\xff\xff'
 b'H\r\x00\x08\xf0\xb5\x89\xb0\x0c"\x00!\x05\xa8\x00\xf0Q\xfa\xa0 \x06#\x03%'
 b'\x02$\x02\xa9\xc0\x05\x02\x93\x03\x94\x04\x95\x00\xf0]\xf8\x18#\xa0 '
 b'\x02\x93\x17;\x03\x93\x00#\x02\xa9\xc0\x05\x06\x93\x05\x93\x07\x93\x04\x95'
 b'\x00\xf0O\xf8!N3x#B\x04\xd0\xff\xf7\xac\xff3x\xa3C3p3x\xdb\x07\x01\xd5'
 b'\xff\xf7^\xff\x0c#7x\x1fB"\xd0\x19M,h\x00,\x14\xd1\xbb\x06:\x07'
 b'\xff\x06\xff\x0f\xb1xpx\xdb\x0f\xd2\x0f\x00\x97\xff\xf7\xff\xfe\x01"'
 b'3x\x99\x06\xc9\x0f\x8aC !R\x01\x8bC\x13C3p\x0eJc\x1c\x13@\x04\xd5 "\x01;RB'
 b'\x13C\x013+`\x14"\x00!\x03\xa8\x00\xf0\xfe\xf9\xa0 \x1e#\x02\xa9\xc0\x05'
 b'\x02\x93\x00\xf0\x0e\xf8\t\xb0\xf0\xbd\xc0F<\x00\x00 8\x00\x00 '
 b'\x1f\x00\x00\x80\xfe\xe7\xfe\xe7pGpGpG\xf0\xb5\x87\xb0\x0bh\x02\x91\x1f"'
 b'\x01!\x01\x93\x05\x00\x01\x98[\x08\x00+\x1e\xd1\x90@ 3\x00(\x02\xd0\x00\xf0'
 b'\xb9\xf9\xc3\xb2\x03\x93\x02\x9b\x03\x9a[h\x04\x93\x01\x9b\xd3@\x16\xd1'
 b'\x04\x9b\x01;\x01+\x08\xd8kh\x01\x9a\x01\x99\x93C\x02\x9a\xd2hJC\x13Ck`\x00 '
 b'\x07\xb0\xf0\xbd\x1c\x00@\x00\x0c@ C\x01:[\x08\xd7\xe7\x01#\x03\x9a\x01\x9c'
 b'\x93@\x01\x9a\x1c@\x1aB\x00\xd1\xd3\xe0f\x08 \x003\x00\x1f"/h\x00+p\xd1\x90@'
 b' 3\x00(\x02\xd0\x00\xf0\x83\xf9\xc3\xb2\x03"[\x00\x9a@ \x00\x97C3\x00'
 b'\x1f"\x00+g\xd1\x90@ 3\x00(\x02\xd0\x00\xf0s\xf9\xc3\xb2\x04\x9a[\x00'
 b'\x9a@\x04\x9b\x17C\x01;/`\x01+$\xd8\x02\x9b \x00\x9bh\x1f"\x05\x933\x00\xafh'
 b'\x00+U\xd1\x90@ 3\x00(\x02\xd0\x00\xf0Z\xf9\xc3\xb2\x03"[\x00\x9a@ \x00\x97C'
 b'3\x00\x1f"\x00+L\xd1\x90@ 3\x00(\x02\xd0\x00\xf0J\xf9\xc3\xb2\x05\x9a'
 b'[\x00\x9a@\x17C\xaf`\x02\x9b \x00\x1bi\x1f"\x05\x933\x00\xefh\x00+>\xd1\x90@'
 b' 3\x00(\x02\xd0\x00\xf05\xf9\xc3\xb2\x03"[\x00\x9a@ \x00\x97C3\x00\x1f"\x00+'
 b'5\xd1\x90@ 3\x00(\x02\xd0\x00\xf0%\xf9\xc3\xb2\x05\x9a[\x00\x9a@\x04\x9b'
 b'\x17C\xef`\x02+_\xd1 \x003\x00\x1f"/\xe0\x01!@\x00\x19@\x08C\x01:[\x08'
 b'\x85\xe7\x01!@\x00\x19@\x08C\x01:[\x08\x8e\xe7\x01!@\x00\x19@\x08C\x01:[\x08'
 b'\xa0\xe7\x01!@\x00\x19@\x08C\x01:[\x08\xa9\xe7\x01!@\x00\x19@\x08C\x01:[\x08'
 b'\xb7\xe7\x01!@\x00\x19@\x08C\x01:[\x08\xc0\xe7\x01!@\x00\x19@\x08C\x01:[\x08'
 b'\x00+\xf7\xd1\x02\x9b\x90@[i\x04\x935\xd0\x00\xf0\xdf\xf8\x07(1\xdc \x00'
 b'3\x00\x1f"/j\x00+\x1d\xd1\x90@ 3\x00(\x02\xd0\x00\xf0\xd1\xf8\xc3\xb2'
 b'\x0f"\x9b\x00\x9a@\x1f#\x97C\x00.\x16\xd1 \x00\x98@ #\x00(\x02\xd0'
 b'\x00\xf0\xc2\xf8\xc3\xb2\x04\x9a\x9b\x00\x9a@\x17C/b\x03\x9b\x013'
 b'\x00\xe7\x01!@\x00\x19@\x08C\x01:[\x08\xd8\xe7\x01 d\x000@\x04C\x01;v\x08'
 b'\xdf\xe7&\nd\n0\x00#\x00\x1f"oj\x00+\x1b\xd1\x90@ 3\x00(\x02\xd0\x00\xf0'
 b'\x9d\xf8\xc3\xb2\x0f"\x9b\x00\x9a@\x1f#\x97C\x00,\x14\xd10\x00\x98@ #'
 b'\x00(\x02\xd0\x00\xf0\x8e\xf8\xc3\xb2\x04\x9a\x9b\x00\x9a@\x17Cob'
 b'\xca\xe7\x01!@\x00\x19@\x08C\x01:[\x08\xda\xe7\x01 v\x00 @\x06C\x01;d\x08'
 b'\xe1\xe7\x00\x00\x03h\x02\x00p\xb5\x01 [\x06,\xd4Nh\x0bhHi3C\xceh\x15h'
 b'3C\x0ei\x0cj3C\x8ei\x03C3C\xcei\x00\x0c3C\x10N#C5@+C\x13`Sh\x8dh\x0eN(C3@'
 b'\x18C\x80#P`\x1b\x01\x9dB\x04\xd2\x80 Sh@\x01\x03CS`\x80#\x00 \x9b\x01'
 b'\x9cB\x02\xd1Kj\x9b\xb2\x13a\xd3i\x03I\x0b@\xd3ap\xbd@\x00\xff\xff'
 b'\xfb\xf0\xff\xff\xff\xf7\xff\xff\x01"\x03h0\xb5\x93C\x03`\xcbh\x8dh\x1b\x02'
 b'\x04h+C\x14M,@#C\x03`Kh\x13L\x03a\x03h\ri\x1aC\x02`\x83h\x8ai#@\x83`\x83h'
 b'*C\xdb\n\xdb\x02\x1aC\x82`\x00-\x04\xd0\x80#\x82h\x1b\x02\x13C\x83`'
 b'\x02h\x08K\x1a@\x0bh\x1aC\x02`ChJi#@\x13CC`\x00 0\xbd\xc0F\xff\xe0\xff\xff'
 b'\xff\x7f\xff\xff\xff\xff\xcf\xff\x1c!\x01#\x1b\x04\x98B\x01\xd3\x00\x0c'
 b'\x109\x1b\n\x98B\x01\xd3\x00\n\x089\x1b\t\x98B\x01\xd3\x00\t\x049\x02\xa2'
 b'\x10\\@\x18pG\xc0F\x04\x03\x02\x02\x01\x01\x01\x01\x00\x00\x00\x00'
 b'\x00\x00\x00\x00\x03\x00\x82\x18\x93B\x00\xd1pG\x19p\x013\xf9\xe7\x00#\xc2\\'
 b'\x013\x00*\xfb\xd1X\x1epG\x00\x00\xf8\xb5\xc0F\xf8\xbc\x08\xbc\x9eFpG'
 b'\xf8\xb5\xc0F\xf8\xbc\x08\xbc\x9eFpG1.1.1\x00OK\x00Bad cmd?\x00Bad args?\x00'
 b'\x00\x00\x00\x00\x00\x00\x00?\x1c\x0e\x00\x1f\x8e\x00\xe0\x0f'
 b'\xf8\xff\x8f\xc7\xe3\xfe?\xe3\xf1\xf8\xff\xf1\xf8\x03\xfe8\xfc\x00\x00\x00'
 b'\x00\x00\x00\x001.1.1 time=20230802.143730 git=q1@6793ed5\x00\x00\x00'
 b'\x00\x00\x00\x00\xe9\x00\x00\x08\xc1\x00\x00\x08')

# EOF
