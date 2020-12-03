package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func calculate_fuel(mass int, recurse bool) int {
	fuel := (mass / 3) - 2
	if (fuel/3-2) > 0 && recurse {
		fuel += calculate_fuel(fuel, recurse)
	}
	return fuel
}

func main() {
	filepath := "input.txt"

	sum_part1 := 0
	sum_part2 := 0

	f, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer func() {
		if err = f.Close(); err != nil {
			log.Fatal(err)
		}
	}()
	s := bufio.NewScanner(f)
	for s.Scan() {
		mass, err := strconv.Atoi(s.Text())
		if err != nil {
			log.Fatal(err)
		}
		sum_part1 += calculate_fuel(mass, false)
		sum_part2 += calculate_fuel(mass, true)
	}
	fmt.Printf("Sum part 1: %v\n", sum_part1)
	fmt.Printf("Sum part 1: %v", sum_part2)
	err = s.Err()
	if err != nil {
		log.Fatal(err)
	}
}
