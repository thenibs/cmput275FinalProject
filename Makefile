# Name: Ahmad Amin, Yash Bhandari & Nibras Alam
# ID: 1623338, 1616539 & 1617818
# CMPUT 275, Winter 2020
#
# Final Prject
#
# Consulted C++ Documentation

CC:=g++
TARGET_DIR:= matpy/target
TARGET:= $(TARGET_DIR)/matpy$(shell python3-config --extension-suffix)
SRC_DIR:= matpy/src
OBJ_DIR:= matpy/obj
SRC:= $(wildcard $(SRC_DIR)/*.cpp)
OBJ:= $(SRC:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)

CFLAGS:= -O3 -Wall -Imatpy/include -std=c++11 -fPIC `python3 -m pybind11 --includes`
LFLAGS:= -shared

all: $(TARGET)

$(TARGET): $(OBJ) | $(TARGET_DIR)
	$(CC) $(OBJ) $(LFLAGS) -o $@

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp | $(OBJ_DIR)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

$(OBJ_DIR):
	mkdir $@

$(TARGET_DIR):
	mkdir $@

.PHONY: python-reqs
python-reqs:
	pip3 install ddt
	pip3 install numpy
	pip3 install pybind11
	pip3 install networkx
	pip3 install matplotlib

.PHONY: test
test:
	python3 -m unittest discover -s tests

.PHONY: clean
clean:
	$(RM) $(OBJ)
	$(RM) $(TARGET)