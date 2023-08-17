from collections import deque

def semantic_stack_pop_beta_times(semantic_stack, var_size_beta):
    while var_size_beta:
        semantic_stack.pop()
        var_size_beta -= 1

    return semantic_stack

def choose_semantic_rule(rule_number, var_rule, var_size_beta, semantic_stack: deque):
    token = {"lexeme": var_rule[0], "class": var_rule[0], "type":"null"}
    # token = eval(f'semantic_rule_{rule_number}({var_rule}, {token}, {var_size_beta}, {semantic_stack.copy()})')
    try:
        token = eval(f'semantic_rule_{rule_number}({var_rule}, {token}, {var_size_beta}, {semantic_stack.copy()})')
    except:
        #print("viado deu erro nos semantics rules: " + rule_number)
        pass
    semantic_stack = semantic_stack_pop_beta_times(semantic_stack, var_size_beta)

    semantic_stack.append(token)

    return semantic_stack

def semantic_rule_0(var_rule, token, var_size_beta, semantic_stack):
    pass

def semantic_rule_1(var_rule, token, var_size_beta, semantic_stack):
    pass

def semantic_rule_2(var_rule, token, var_size_beta, semantic_stack):
    pass

def semantic_rule_3(var_rule, token, var_size_beta, semantic_stack):
    pass
def semantic_rule_4(var_rule, token, var_size_beta, semantic_stack):
    pass

def semantic_rule_5(var_rule, token, var_size_beta, semantic_stack):
    return token, semantic_stack

def semantic_rule_6(var_rule, token, var_size_beta, semantic_stack):
    semantic_stack.pop()
    tmp_l = semantic_stack.pop()
    print(f' {tmp_l["lexeme"]};')
    #func q amarra o proximo pop com os ids
    return token

def semantic_rule_7(var_rule, token, var_size_beta, semantic_stack):
    tmp_l = semantic_stack.pop()
    tmp_vir = semantic_stack.pop()
    tmp_id = semantic_stack.pop()

    token["lexeme"] = tmp_id["lexeme"] + tmp_vir["lexeme"] + tmp_l["lexeme"]

    return token

def semantic_rule_8(var_rule, token, var_size_beta, semantic_stack):
    tmp_token = semantic_stack.pop()
    token["lexeme"] = tmp_token["lexeme"]

    return token

def semantic_rule_9(var_rule, token, var_size_beta, semantic_stack):
    token["type"] = "int"
    print(token["type"], end="")

    return token

def semantic_rule_10(var_rule, token, var_size_beta, semantic_stack):
    token["type"] = "double"
    print(token["type"])

    return token

def semantic_rule_11(var_rule, token, var_size_beta, semantic_stack):
    token["type"] = "literal"
    print(token["type"])

    return token

def semantic_rule_13(var_rule, token, var_size_beta, semantic_stack):
    semantic_stack.pop()
    print(f'scanf(“%d”, &{semantic_stack[-1]["lexeme"]});')

    return token

def semantic_rule_14(var_rule, token, var_size_beta, semantic_stack):

    semantic_stack.pop()
    print(f'printf(“{str(semantic_stack.pop()["lexeme"])}”)')
    return token

def semantic_rule_15(var_rule, token, var_size_beta, semantic_stack):
    token = semantic_stack.pop()

    return token


def semantic_rule_16(var_rule, token, var_size_beta, semantic_stack):
    token = semantic_stack.pop()

    return token

def semantic_rule_17(var_rule, token, var_size_beta, semantic_stack):
    token = semantic_stack.pop()

    return token

def semantic_rule_19(var_rule, token, var_size_beta, semantic_stack):
    tmp_ptv = semantic_stack.pop()
    tmp_ld = semantic_stack.pop()
    tmp_rcb = semantic_stack.pop()
    tmp_id = semantic_stack.pop()

    print(f'{tmp_id["lexeme"]} {tmp_rcb["lexeme"]} {tmp_ld["lexeme"]}')

    return token

def semantic_rule_20(var_rule, token, var_size_beta, semantic_stack):
    tmp_oprd_2 = semantic_stack.pop()
    tmp_opm = semantic_stack.pop()
    tmp_oprd_1 = semantic_stack.pop()
    token["lexeme"] = tmp_oprd_1["lexeme"] + " " + tmp_opm["lexeme"] + " " + tmp_oprd_2["lexeme"]

    return token

def semantic_rule_21(var_rule, token, var_size_beta, semantic_stack):
    tmp_token = semantic_stack.pop()
    token["lexeme"] = tmp_token["lexeme"]
    token["type"] = tmp_token["type"]

    return token

def semantic_rule_22(var_rule, token, var_size_beta, semantic_stack):
    tmp_token = semantic_stack.pop()
    token["lexeme"] = tmp_token["lexeme"]
    token["type"] = tmp_token["type"]

    return token

def semantic_rule_23(var_rule, token, var_size_beta, semantic_stack):
    tmp_token = semantic_stack.pop()
    token["lexeme"] = tmp_token["lexeme"]
    token["type"] = tmp_token["type"]

    return token

def semantic_rule_25(var_rule, token, var_size_beta, semantic_stack):
    print("}")

    return token

def semantic_rule_26(var_rule, token, var_size_beta, semantic_stack):
    semantic_stack.pop()
    semantic_stack.pop()
    tmp_expr = semantic_stack.pop()

    print(f'if({tmp_expr["lexeme"]})', end="")
    print("{")

    return token

def semantic_rule_27(var_rule, token, var_size_beta, semantic_stack):
    tmp_oprd_2 = semantic_stack.pop()
    tmp_opr = semantic_stack.pop()
    tmp_oprd_1 = semantic_stack.pop()
    token["lexeme"] = tmp_oprd_1["lexeme"] + " " + tmp_opr["lexeme"] + " " + tmp_oprd_2["lexeme"]

    return token

def semantic_rule_32(var_rule, token, var_size_beta, semantic_stack):


    return token

def semantic_rule_33(var_rule, token, var_size_beta, semantic_stack):
    print("}")

    return token

def semantic_rule_34(var_rule, token, var_size_beta, semantic_stack):
    semantic_stack.pop()
    tmp_expr = semantic_stack.pop()
    print(f'while({tmp_expr["lexeme"]})', end="")
    print("{")

    return token