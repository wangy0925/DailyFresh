.SUFFIXES: .c .o

COMPILE = $(CC) -Wall -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -g -O -DDEBUG_FLAG -DOS_FREEBSD -DIOEVENT_USE_KQUEUE -DDARWIN
INC_PATH = -I. -Itrunk_mgr -I../common -I../tracker -I../client -Ifdht_client -I/usr/include/fastcommon
LIB_PATH = -L/usr/local/lib  -lfastcommon
TARGET_PATH = /usr/bin
CONFIG_PATH = /etc/fdfs

SHARED_OBJS = ../common/fdfs_global.o \
              ../tracker/fdfs_shared_func.o ../tracker/tracker_proto.o \
              tracker_client_thread.o storage_global.o storage_func.o \
              storage_service.o storage_sync.o storage_nio.o storage_dio.o \
              storage_ip_changed_dealer.o storage_param_getter.o \
              storage_disk_recovery.o trunk_mgr/trunk_mem.o \
              trunk_mgr/trunk_shared.o trunk_mgr/trunk_sync.o \
              trunk_mgr/trunk_client.o trunk_mgr/trunk_free_block_checker.o \
              ../client/client_global.o ../client/tracker_client.o \
              ../client/storage_client.o ../client/client_func.o \
              fdht_client/fdht_proto.o fdht_client/fdht_client.o \
              fdht_client/fdht_func.o fdht_client/fdht_global.o \
               storage_dump.o

ALL_OBJS = $(SHARED_OBJS)

ALL_PRGS = fdfs_storaged 

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
	if [ ! -f $(CONFIG_PATH)/storage.conf.sample ]; then cp -f ../conf/storage.conf $(CONFIG_PATH)/storage.conf.sample; fi
clean:
	rm -f $(ALL_OBJS) $(ALL_PRGS)
