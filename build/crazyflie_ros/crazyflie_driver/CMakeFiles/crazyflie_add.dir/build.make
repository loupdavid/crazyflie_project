# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/bitcraze/ros_workspace/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/bitcraze/ros_workspace/build

# Include any dependencies generated for this target.
include crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/depend.make

# Include the progress variables for this target.
include crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/progress.make

# Include the compile flags for this target's objects.
include crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/flags.make

crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o: crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/flags.make
crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o: /home/bitcraze/ros_workspace/src/crazyflie_ros/crazyflie_driver/src/crazyflie_add.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/bitcraze/ros_workspace/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o"
	cd /home/bitcraze/ros_workspace/build/crazyflie_ros/crazyflie_driver && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o -c /home/bitcraze/ros_workspace/src/crazyflie_ros/crazyflie_driver/src/crazyflie_add.cpp

crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.i"
	cd /home/bitcraze/ros_workspace/build/crazyflie_ros/crazyflie_driver && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/bitcraze/ros_workspace/src/crazyflie_ros/crazyflie_driver/src/crazyflie_add.cpp > CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.i

crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.s"
	cd /home/bitcraze/ros_workspace/build/crazyflie_ros/crazyflie_driver && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/bitcraze/ros_workspace/src/crazyflie_ros/crazyflie_driver/src/crazyflie_add.cpp -o CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.s

crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o.requires:
.PHONY : crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o.requires

crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o.provides: crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o.requires
	$(MAKE) -f crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/build.make crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o.provides.build
.PHONY : crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o.provides

crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o.provides.build: crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o

# Object files for target crazyflie_add
crazyflie_add_OBJECTS = \
"CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o"

# External object files for target crazyflie_add
crazyflie_add_EXTERNAL_OBJECTS =

/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/build.make
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/libtf.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/libtf2_ros.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/libactionlib.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/libmessage_filters.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/libroscpp.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /usr/lib/i386-linux-gnu/libboost_signals.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /usr/lib/i386-linux-gnu/libboost_filesystem.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/libxmlrpcpp.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/libtf2.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/libroscpp_serialization.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/librosconsole.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/librosconsole_log4cxx.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/librosconsole_backend_interface.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /usr/lib/liblog4cxx.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /usr/lib/i386-linux-gnu/libboost_regex.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/librostime.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /usr/lib/i386-linux-gnu/libboost_date_time.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/ros/indigo/lib/libcpp_common.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /usr/lib/i386-linux-gnu/libboost_system.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /usr/lib/i386-linux-gnu/libboost_thread.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /usr/lib/i386-linux-gnu/libpthread.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /usr/lib/i386-linux-gnu/libconsole_bridge.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /home/bitcraze/ros_workspace/devel/lib/libcrazyflie_cpp.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: /opt/gnuarmeclipse/openocd/0.9.0-201505190955/bin/libusb-1.0.so
/home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add: crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable /home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add"
	cd /home/bitcraze/ros_workspace/build/crazyflie_ros/crazyflie_driver && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/crazyflie_add.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/build: /home/bitcraze/ros_workspace/devel/lib/crazyflie_driver/crazyflie_add
.PHONY : crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/build

crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/requires: crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/src/crazyflie_add.cpp.o.requires
.PHONY : crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/requires

crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/clean:
	cd /home/bitcraze/ros_workspace/build/crazyflie_ros/crazyflie_driver && $(CMAKE_COMMAND) -P CMakeFiles/crazyflie_add.dir/cmake_clean.cmake
.PHONY : crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/clean

crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/depend:
	cd /home/bitcraze/ros_workspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/bitcraze/ros_workspace/src /home/bitcraze/ros_workspace/src/crazyflie_ros/crazyflie_driver /home/bitcraze/ros_workspace/build /home/bitcraze/ros_workspace/build/crazyflie_ros/crazyflie_driver /home/bitcraze/ros_workspace/build/crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : crazyflie_ros/crazyflie_driver/CMakeFiles/crazyflie_add.dir/depend

