.SUFFIXES: .c .o

COMPILE = $(CC) -Wall -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -g -O -DDEBUG_FLAG -DOS_FREEBSD -DIOEVENT_USE_KQUEUE -DDARWIN
INC_PATH = -I/usr/include/fastcommon -I/usr/include/fastdfs
LIB_PATH = -L/usr/local/lib -lfastcommon -lfdfsclient 
TARGET_PATH = $(TARGET_PATH)

ALL_OBJS = 

ALL_PRGS = fdfs_monitor fdfs_test fdfs_test1

all: $(ALL_OBJS) $(ALL_PRGS)
.o:
	$(COMPILE) -o $@ $<  $(SHARED_OBJS) $(LIB_PATH) $(INC_PATH)
.c:
	$(COMPILE) -o $@ $<  $(ALL_OBJS) $(LIB_PATH) $(INC_PATH)
.c.o:
	$(COMPILE) -c -o $@ $<  $(INC_PATH)
install:
	cp -f $(ALL_PRGS) $(TARGET_PATH)
clean:
	rm -f $(ALL_OBJS) $(ALL_PRGS)

