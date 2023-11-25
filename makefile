# Compile c++ code

# Compiler
CC = g++

# Compiler flags
CFLAGS = -Wall -Wextra -Werror -pedantic -std=c++17 -O3

# Source files
SRC = $(wildcard *.cpp)

# Object files
OBJ = $(SRC:.cpp=.o)

# Executable
EXEC = main

# Compile
all: $(EXEC)

$(EXEC): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(EXEC)

%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(EXEC)