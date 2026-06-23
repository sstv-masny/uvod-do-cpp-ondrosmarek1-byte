#!/usr/bin/env python3
"""
Test runner for C++ function practice tasks.
Compiles each task and runs it against all test cases.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Task directories
TASKS = [
    "task_01_even_or_odd",
    "task_02_min_of_three",
    "task_03_taxi_fare",
    "task_04_leap_year",
    "task_05_sum_1_to_n",
    "task_06_reverse_digits",
    "task_07_gcd_fraction",
    "task_08_frequency_table",
    "task_09_palindrome",
    "task_10_binary_search_first",
]


def compile_task(task_dir: Path) -> Tuple[bool, str]:
    """Compile the main.cpp file in the task directory."""
    main_cpp = task_dir / "main.cpp"
    executable = task_dir / "solution"

    if not main_cpp.exists():
        return False, f"main.cpp not found in {task_dir}"

    # Compile with C++11 standard and warnings
    cmd = [
        "g++",
        "-std=c++11",
        "-Wall",
        "-Wextra",
        "-o",
        str(executable),
        str(main_cpp),
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)

        if result.returncode != 0:
            return False, result.stderr

        return True, ""
    except subprocess.TimeoutExpired:
        return False, "Compilation timeout"
    except Exception as e:
        return False, str(e)


def run_test(
    executable: Path, input_file: Path, output_file: Path
) -> Tuple[bool, str, str]:
    """Run a single test case."""
    if not input_file.exists():
        return False, "", f"Input file {input_file} not found"

    if not output_file.exists():
        return False, "", f"Output file {output_file} not found"

    try:
        # Run the executable with input
        with open(input_file, "r") as f_in:
            result = subprocess.run(
                [str(executable)], stdin=f_in, capture_output=True, text=True, timeout=5
            )

        if result.returncode != 0:
            return False, result.stdout, f"Runtime error: {result.stderr}"

        # Compare output
        actual_output = result.stdout.strip()
        with open(output_file, "r") as f:
            expected_output = f.read().strip()

        if actual_output == expected_output:
            return True, actual_output, ""
        else:
            return (
                False,
                actual_output,
                f"Expected:\n{expected_output}\n\nGot:\n{actual_output}",
            )

    except subprocess.TimeoutExpired:
        return False, "", "Test timeout (5 seconds)"
    except Exception as e:
        return False, "", str(e)


def test_task(task_dir: Path) -> Tuple[int, int]:
    """Test a single task. Returns (passed, total)."""
    print(f"\n{BLUE}Testing {task_dir.name}...{RESET}")

    # Compile the task
    success, error = compile_task(task_dir)
    if not success:
        print(f"  {RED}✗ Compilation failed{RESET}")
        if error:
            print(f"    {error}")
        return 0, 0

    print(f"  {GREEN}✓ Compilation successful{RESET}")

    # Find all test cases
    test_dir = task_dir / "tests"
    if not test_dir.exists():
        print(f"  {YELLOW}⚠ No test directory found{RESET}")
        return 0, 0

    # Get all .in files
    input_files = sorted(test_dir.glob("*.in"))
    if not input_files:
        print(f"  {YELLOW}⚠ No test cases found{RESET}")
        return 0, 0

    executable = task_dir / "solution"
    passed = 0
    total = 0

    for input_file in input_files:
        output_file = input_file.with_suffix(".out")
        test_name = input_file.stem

        success, actual, error = run_test(executable, input_file, output_file)
        total += 1

        if success:
            passed += 1
            print(f"  {GREEN}✓{RESET} Test {test_name} passed")
        else:
            print(f"  {RED}✗{RESET} Test {test_name} failed")
            if error:
                print(f"    {error}")

    # Clean up executable
    if executable.exists():
        executable.unlink()

    return passed, total


def main():
    """Main test runner."""
    print(f"{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}C++ Function Practice Tasks - Test Runner{RESET}")
    print(f"{BLUE}{'='*60}{RESET}")

    script_dir = Path(__file__).parent
    total_passed = 0
    total_tests = 0

    # Store results for summary table
    task_results = []

    for task_name in TASKS:
        task_dir = script_dir / task_name

        if not task_dir.exists():
            print(f"\n{YELLOW}⚠ Skipping {task_name} (directory not found){RESET}")
            continue

        passed, tests = test_task(task_dir)
        total_passed += passed
        total_tests += tests

        # Store result for this task
        task_results.append({"name": task_name, "passed": passed, "total": tests})

    # Summary
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Summary{RESET}")
    print(f"{BLUE}{'='*60}{RESET}")

    if total_tests == 0:
        print(f"{YELLOW}No tests were run{RESET}")
        return 1

    # Display summary table
    print(f"\n{'Task':<35} {'Passed':<10} {'Total':<10} {'Status'}")
    print(f"{'-'*35} {'-'*10} {'-'*10} {'-'*10}")

    for result in task_results:
        task_name = result["name"]
        passed = result["passed"]
        total = result["total"]

        if total == 0:
            status = f"{YELLOW}NO TESTS{RESET}"
        elif passed == total:
            status = f"{GREEN}✓ PASS{RESET}"
        else:
            status = f"{RED}✗ FAIL{RESET}"

        print(f"{task_name:<35} {passed:<10} {total:<10} {status}")

    print(f"{'-'*35} {'-'*10} {'-'*10} {'-'*10}")
    print(f"{'TOTAL':<35} {total_passed:<10} {total_tests:<10}")

    percentage = (total_passed / total_tests * 100) if total_tests > 0 else 0

    print(f"\n{BLUE}Overall Result:{RESET}", end=" ")
    if total_passed == total_tests:
        print(
            f"{GREEN}All tests passed! ({total_passed}/{total_tests} - 100.0%){RESET}"
        )
        return 0
    else:
        print(
            f"{RED}Some tests failed: {total_passed}/{total_tests} passed ({percentage:.1f}%){RESET}"
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
