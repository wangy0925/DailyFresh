.SUFFIXES: .c .o

COMPILE = $(CC) -Wall -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -g -O -DDEBUG_FLAG -DOS_FREEBSD -DIOEVENT_USE_KQUEUE -DDARWIN
INC_PATH = -I../common -I/usr/include/fastcommon
LIB_PATH = -L/usr/local/lib  -lfastcommon
TARGET_PATH = /usr/bin
CONFIG_PATH = /etc/fdfs

SHARED_OBJS = ../common/fdfs_global.o \
              tracker_proto.o tracker_mem.o tracker_service.o tracker_status.o \
              tracker_global.o tracker_func.o \
              fdfs_shared_func.o tracker_nio.o tracker_relationship.o \
               tracker_dump.o

ALL_OBJS = $(SHARED_OBJS)

ALL_PRGS = fdfs_trackerd

all: $(ALL_OBJS) $(ALL_PRGS)
.o:
	$(COMPILE) -o $@ $<  $(SHARED_OBJS) $(LIB_PATH) $(INC_PATH)
.c:
	$(COMPILE) -o $@ $<  $(ALL_OBJS) $(LIB_PATH) $(INC_PATH)
.c.o:
	$(COMPILE) -c -o $@ $<  $(INC_PATH)
install:
	mkdir -p $(TARGET_PATH)
	mkdir -p $(CONFIG_PATH)
	cp -f $(ALL_PRGS) $(TARGET_PATH)
	if [ ! -f $(CONFIG_PATH)/tracker.conf.sample ]; then cp -f ../conf/tracker.conf $(CONFIG_PATH)/tracker.conf.sample; fi
clean:
	rm -f $(ALL_OBJS) $(ALL_PRGS)
