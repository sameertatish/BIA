from django.shortcuts import render
import sys
import os

# Add the directory containing the 'main' module to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import (
    read_tasks_times,
    read_links,
    get_all_solutions,
    get_best_solution,
    write_solution_list,
    write_solution,
)

def members(request):
    # Reading the results files
    with open("optimal_results_steps.txt", "r") as file:
        optimal_results = file.read()

    with open("all_results_steps.txt", "r") as file:
        all_results = file.read()

    context = {
        "optimal_results": optimal_results,
        "all_results": all_results,
    }

    return render(request, "results.html")

def save_all_results(request):
    # Generate the results
    tasks_times = read_tasks_times()
    links = read_links(tasks_times)
    steps = 3

    solutions = get_all_solutions(tasks_times, links, steps)
    write_solution_list(solutions, "all_results_steps.txt")

    # Read the all_results file
    with open("all_results_steps.txt", "r") as file:
        all_results = file.read()

    context = {
        "all_results": all_results,
    }

    return render(request, "results.html", context)

def show_best_result(request):
    # Generate the results
    tasks_times = read_tasks_times()
    links = read_links(tasks_times)
    steps = 3

    solutions = get_all_solutions(tasks_times, links, steps)
    best_solution = get_best_solution(solutions)
    write_solution(best_solution, "optimal_results_steps.txt")

    # Read the optimal_results file
    with open("optimal_results_steps.txt", "r") as file:
        optimal_results = file.read()

    context = {
        "optimal_results": optimal_results,
    }

    return render(request, "results.html", context)


