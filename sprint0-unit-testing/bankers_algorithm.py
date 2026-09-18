from typing import List, Tuple

# Need = Max − Allocation; it shows how many more resources each process requires to finish
def calculate_need_matrix(
    allocation: List[List[int]],
    max_need: List[List[int]]
) -> List[List[int]]:
    need = []

    # Iterate over each process (i)
    for i in range(len(allocation)):
        row = []
        # Iterate over each resource type (j)
        for j in range(len(allocation[i])):
            # Subtract allocated from maximum to get remaining need
            row.append(max_need[i][j] - allocation[i][j])
        need.append(row)

    return need


# Simulate processes finishing one by one; if all can finish, the state is SAFE, otherwise UNSAFE
def safety_algorithm(
    processes: List[str],          
    allocation: List[List[int]],
    need: List[List[int]],
    available: List[int]
) -> Tuple[bool, List[str]]:

    # Initialize the work resource pool
    work = available.copy()

    # All processes start unfinished
    # Finish[i] tracks whether process i has been completed safely
    finish = [False] * len(processes)

    safe_sequence: List[str] = []
    step = 1

    print("Initial Work:", work)
    print()

    # Loop until no more processes can be added to safe sequence
    while False in finish:
        found = False

        # Try to find an unfinished process that can complete
        for i in range(len(processes)):
            if not finish[i]:
                can_allocate = True # Check if process can be allocated to needed resources

                # If any Need[i][j] > Work[j], this process cannot run so skip it
                for j in range(len(work)):
                    if need[i][j] > work[j]:
                        can_allocate = False
                        break

                # Process is safe to run; assume it finishes and releases its resources to Work
                if can_allocate:
                    print(f"Step #{step}:")
                    print(f"Selected {processes[i]}")
                    print(f"Need: {need[i]}") # What this process still wanted
                    print(f"Work Before: {work}") # Available resources before release

                    # Record this process in the safe sequence
                    safe_sequence.append(processes[i])
                    finish[i] = True # Mark as finished so we skip it next pass

                    # When a process finishes it releases everything it was holding
                    for j in range(len(work)):
                        work[j] += allocation[i][j]

                    print(f"Work After: {work}")
                    print(f"Finish: {finish}")
                    print()

                    step += 1
                    found = True
                    break

        # If we scanned every unfinished process and none had Need[i] ≤ Work, system is deadlocked
        if not found:
            return False, [] # UNSAFE, return empty sequence

    # If the while loop exits normally, every process reached Finish[i]=True
    return True, safe_sequence


# Calculate the Need matrix (what each process still wants)
# Run the Safety Algorithm to determine if the state is safe
def bankers_algorithm(
    processes: List[str],
    allocation: List[List[int]],
    max_need: List[List[int]],
    available: List[int]
) -> Tuple[bool, List[str]]:

    # Get the Need matrix from Max and Allocation
    need = calculate_need_matrix(allocation, max_need)

    # Print the Allocation Matrix
    # P1: [0,1,0], P2: [2,0,0], P3: [3,0,2], P4: [2,1,1], P5: [0,0,2]
    print("Allocation Matrix:")
    for i in range(len(processes)):
        print(f"{processes[i]}: {allocation[i]}")
    print()

    # Print the Need matrix
    # P1: [7,4,3], P2: [1,2,2], P3: [6,0,0], P4: [0,1,1], P5: [4,3,1]
    print("Need Matrix:")
    for i in range(len(processes)):
        print(f"{processes[i]}: {need[i]}")
    print()

    return safety_algorithm(processes, allocation, need, available)


if __name__ == "__main__":

    # Index 0 = P1, index 1 = P2, etc
    processes = ["P1", "P2", "P3", "P4", "P5"]

    allocation = [
        [0, 1, 0], # P1 holds: A=0, B=1, C=0
        [2, 0, 0], # P2 holds: A=2, B=0, C=0
        [3, 0, 2], # P3 holds: A=3, B=0, C=2
        [2, 1, 1], # P4 holds: A=2, B=1, C=1
        [0, 0, 2]  # P5 holds: A=0, B=0, C=2
    ]

    max_need = [
        [7, 5, 3], # P1 can request up to A=7, B=5, C=3
        [3, 2, 2], # P2 can request up to A=3, B=2, C=2
        [9, 0, 2], # P3 can request up to A=9, B=0, C=2
        [2, 2, 2], # P4 can request up to A=2, B=2, C=2
        [4, 3, 3]  # P5 can request up to A=4, B=3, C=3
    ]

    # Resources that are currently free 
    available = [3, 3, 2]

    # Run the algorithm
    safe, sequence = bankers_algorithm(processes, allocation, max_need, available)

    # Report the outcome
    if safe:
        print("The system is SAFE")
        # P2 -> P4 -> P1 -> P3 -> P5
        print("Safe sequence:", " -> ".join(sequence))
    else:
        print("The system is UNSAFE")