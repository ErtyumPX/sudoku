CC := g++
CFLAGS := -Wall -std=c++11 -Iinclude
LDFLAGS := 

SRC_DIR := src
OBJ_DIR := build
BIN_DIR := bin

SRC := $(wildcard $(SRC_DIR)/*.cpp)
OBJ := $(patsubst $(SRC_DIR)/%.cpp, $(OBJ_DIR)/%.o, $(SRC))
EXECUTABLE := $(BIN_DIR)/test

.PHONY: all clean run

all: clean $(EXECUTABLE)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -c $< -o $@

$(EXECUTABLE): $(OBJ)
	$(CC) $^ -o $@ $(LDFLAGS)

clean:
	rm -f $(OBJ_DIR)/*.o $(EXECUTABLE)

run: $(EXECUTABLE)
	./$(EXECUTABLE)

