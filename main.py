"""
 x1 + 2y1 + z1 ==  0
2x2 -  y2 + z2 ==  1
-x3 + 3y3 + z3 == -2

Matriz:

Regra de Cramer -> x == Dx/D, y == Dy/D, z == Dz/D

D:
| 1  2  1 |  1   2    Multiplica as diagonais da direita para esquerda e da esquerda para a direita
| 2 -1  1 |  2  -1 -> (1*-1*1 + 2*1*-1 + 1*2*3) - (2*2*1 + 1*1*3 + 1*-1*-1) == 3 - 8 == -5, logo, D == -5
|-1  3  1 | -1   3

Dx:
| 0  2  1 |  0   2    Substitui a primeira fileira pelos valores adjacentes
| 1 -1  1 |  1  -1 -> (0*-1*1 + 2*1*-2 + 1*1*3) - (2*1*1 + 0*1*3 + 1*-1*-2) == -1 - 4 == -5, logo, Dx == -5
|-2  3  1 | -2   3

Dy:
| 1  0  1 |  1   0    Substitui a segunda fileira pelos valores adjacentes
| 2  1  1 |  2   1 -> (1*1*1 + 0*1*-1 + 1*2*-2) - (0*2*1 + 1*1*-2 + 1*1*-1) == -3 - (-3) == 0, logo, Dy == 0
|-1 -2  1 | -1  -2

Dz:
| 1  2  0 |  1   2    Substitui a terceira fileira pelos valores adjacentes
| 2 -1  1 |  2  -1 -> (1*-1*-2 + 2*1*-1 + 0*2*3) - (2*2*-2 + 1*1*3 + 0*-1*-1) == 0 - (-5) == 5, logo, Dz == 5
|-1  3 -2 | -1   3

x == -5/-5 == 1
y == 0/-5 == 0
z == 5/-5 == -1

Prova real:
1 + 2*0 + (-1) == 0
2*1 - 0 + (-1) == 1
-1 + 3*0 + (-1) == -2
"""


def ret(var: str, num: int, val: dict) -> int:
    return val.get(f"{var}{num}")


def calculate_d(values: dict) -> int:
    # d_sumv = []
    # d_subtv = []
    # variables_sum = ['x', 'y', 'z']
    # variables_subt = ['y', 'x', 'z']
    #
    # # Sum
    # for count1 in range(3):
    #     dm = {}
    #     for count2 in range(3):
    #         dm.update({variables_sum[count2]: values.get(f"{variables_sum[count2]}{count1 + 1}")})
    #     removed = variables_sum[0]
    #     variables_sum.append(removed)
    #     d_sumv.append(int(dm.get(f"x{count1 + 1}")) * int(dm.get(f"y{count1 + 1}")) * int(dm.get(f"z{count1 + 1}")))
    #
    # # Subt
    # for count1 in range(3):
    #     dm = {}
    #     for count2 in range(3):
    #         dm.update({variables_subt[count2]: values.get(f"{variables_subt[count2]}{count1 + 1}")})
    #     removed = variables_subt[0]
    #     variables_subt.append(removed)
    #     d_subtv.append(int(dm.get(f"x{count1 + 1}")) * int(dm.get(f"y{count1 + 1}")) * int(dm.get(f"z{count1 + 1}")))
    #
    # return d_sumv[0] + d_sumv[1] + d_sumv[2] - d_subtv[0] - d_subtv[1] - d_subtv[2]

    # **********

    d_1_sum = ret(var="x", num=1, val=values) * ret(var="y", num=2, val=values) * ret(var="z", num=3, val=values)
    d_2_sum = ret(var="y", num=1, val=values) * ret(var="z", num=2, val=values) * ret(var="x", num=3, val=values)
    d_3_sum = ret(var="z", num=1, val=values) * ret(var="x", num=2, val=values) * ret(var="y", num=3, val=values)
    d_sum = d_1_sum + d_2_sum + d_3_sum

    d_1_subt = ret(var="y", num=1, val=values) * ret(var="x", num=2, val=values) * ret(var="z", num=3, val=values)
    d_2_subt = ret(var="x", num=1, val=values) * ret(var="z", num=2, val=values) * ret(var="y", num=3, val=values)
    d_3_subt = ret(var="z", num=1, val=values) * ret(var="y", num=2, val=values) * ret(var="x", num=3, val=values)
    d_subt = d_1_subt + d_2_subt + d_3_subt

    return d_sum - d_subt


def calculate_dx(values: dict, results: dict) -> int:
    d_1_sum = int(results.get("result_1")) * ret(var="y", num=2, val=values) * ret(var="z", num=3, val=values)
    d_2_sum = ret(var="y", num=1, val=values) * ret(var="z", num=2, val=values) * int(results.get("result_3"))
    d_3_sum = ret(var="z", num=1, val=values) * int(results.get("result_2")) * ret(var="y", num=3, val=values)
    d_sum = d_1_sum + d_2_sum + d_3_sum

    d_1_subt = ret(var="y", num=1, val=values) * int(results.get("result_2")) * ret(var="z", num=3, val=values)
    d_2_subt = int(results.get("result_1")) * ret(var="z", num=2, val=values) * ret(var="y", num=3, val=values)
    d_3_subt = ret(var="z", num=1, val=values) * ret(var="y", num=2, val=values) * int(results.get("result_3"))
    d_subt = d_1_subt + d_2_subt + d_3_subt

    return d_sum - d_subt


def calculate_dy(values: dict, results: dict) -> int:
    d_1_sum = ret(var="x", num=1, val=values) * int(results.get("result_2")) * ret(var="z", num=3, val=values)
    d_2_sum = int(results.get("result_1")) * ret(var="z", num=2, val=values) * ret(var="x", num=3, val=values)
    d_3_sum = ret(var="z", num=1, val=values) * ret(var="x", num=2, val=values) * int(results.get("result_3"))
    d_sum = d_1_sum + d_2_sum + d_3_sum

    d_1_subt = int(results.get("result_1")) * ret(var="x", num=2, val=values) * ret(var="z", num=3, val=values)
    d_2_subt = ret(var="x", num=1, val=values) * ret(var="z", num=2, val=values) * int(results.get("result_3"))
    d_3_subt = ret(var="z", num=1, val=values) * int(results.get("result_2")) * ret(var="x", num=3, val=values)
    d_subt = d_1_subt + d_2_subt + d_3_subt

    return d_sum - d_subt


def calculate_dz(values: dict, results: dict) -> int:
    d_1_sum = ret(var="x", num=1, val=values) * ret(var="y", num=2, val=values) * int(results.get("result_3"))
    d_2_sum = ret(var="y", num=1, val=values) * int(results.get("result_2")) * ret(var="x", num=3, val=values)
    d_3_sum = int(results.get("result_1")) * ret(var="x", num=2, val=values) * ret(var="y", num=3, val=values)
    d_sum = d_1_sum + d_2_sum + d_3_sum

    d_1_subt = ret(var="y", num=1, val=values) * ret(var="x", num=2, val=values) * int(results.get("result_3"))
    d_2_subt = ret(var="x", num=1, val=values) * int(results.get("result_2")) * ret(var="y", num=3, val=values)
    d_3_subt = int(results.get("result_1")) * ret(var="y", num=2, val=values) * ret(var="x", num=3, val=values)
    d_subt = d_1_subt + d_2_subt + d_3_subt

    return d_sum - d_subt


def main(order: dict, results: dict) -> dict:
    d = calculate_d(values=order)
    # print(f"D: {d}")

    dx = calculate_dx(values=order, results=results)
    # print(f"Dx: {dx}")

    dy = calculate_dy(values=order, results=results)
    # print(f"Dy: {dy}")

    dz = calculate_dz(values=order, results=results)
    # print(f"Dz: {dz}")

    return {"x": dx/d, "y": dy/d, "z": dz/d}


# Informar o valor de x, y e z em cada linha do sistema
if __name__ == "__main__":
    print("""Este programa foi feito para resolver sistemas de 3 linhas utilizando a lógica das matrizes.
A base é:
     x1 + y1 + z1 ==  r1
     x2 + y2 + z2 ==  r2
     x3 + y3 + z3 ==  r3""")
    variables = ['x', 'y', 'z']
    results_list = [str(f"result_{i + 1}") for i in range(3)]
    results = {}
    order = {}

    for count in range(len(results_list)):
        data = int(input(f"Resultado da parte {count + 1} do sistema (r{count + 1}): "))
        results.update({f"{results_list[count]}": data})

    for count1 in range(3):
        for count2 in range(len(variables)):
            data = int(input(f"{variables[count2]}{count1 + 1}: "))
            order.update({f"{variables[count2]}{count1 + 1}": data})

    values = main(order=order, results=results)
    print(f"x == {values.get('x')}\n"
          f"y == {values.get('y')}\n"
          f"z == {values.get('z')}\n")
