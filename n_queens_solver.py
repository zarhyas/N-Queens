board_size = 8
full_board_mask = (2**board_size) - 1


def queens(row_mask, left_diagonal_mask, right_diagonal_mask, current_solution, all_solutions):

    unsafe_spots_mask = full_board_mask & (
        row_mask | left_diagonal_mask | right_diagonal_mask)

    for i in range(board_size):

        queen_mask = 1 << i

        if queen_mask & unsafe_spots_mask == 0:
            nxRow_mask = row_mask | queen_mask
            nxLeft_diagonal_mask = (left_diagonal_mask | queen_mask) << 1
            nxRight_diagonal_mask = (right_diagonal_mask | queen_mask) >> 1
            solution = current_solution + [queen_mask]

            if nxRow_mask == full_board_mask:
                all_solutions.append(solution)
                return

            else:
                queens(nxRow_mask, nxLeft_diagonal_mask,
                       nxRight_diagonal_mask, solution, all_solutions)

    return all_solutions


solutions = queens(0, 0, 0, [], [])

for solution in solutions:
    print("\n".join(["{0:b}".format(num).zfill(board_size)
          for num in solution]) + "\n")

print("Number of solutions : %d" % len(solutions))
