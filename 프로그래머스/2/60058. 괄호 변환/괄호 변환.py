import collections
def solution(p):
    def recursive(p):
        answer = []
        if not p:  # 빈 문자열 처리
            return ""
        u, v = "", ""
        for e in range(1,len(p)+1):
            if p[:e].count("(") == p[:e].count(")"):
                u = p[:e]
                v = p[e:]
                break
        if not u:  # u가 설정되지 않았을 경우 처리
            return p  # 또는 다른 적절한 처리

        stack = [u[0]]
        for e in range(1,len(u)):
            if stack[-1] == "(" and u[e] == ")":
                stack.pop()
            else:
                stack.append(u[e])
        if len(stack) != 0 :
            answer += "("
            answer += recursive(v)
            answer += ")"
            u = u[1:-1]
            for i in u:
                if i == "(":
                    answer += ")"
                else:
                    answer += "("
        else:
            answer += u
            answer += recursive(v)
        return answer
    
    ar = recursive(p)
    answer = ''.join(ar)
    return answer