def solution(begin, target, words):

    def CanChange(s,t):
        diff = 0
        for s_ , t_ in zip(s,t):
            if s_ != t_:
                diff +=1
        if diff == 1:
            return True
        else: return False

    if target not in words:
        return 0

    answers=[]
    visited = {}

    def dfs(s,dep):
        if s == target:
            answers.append(dep)

        if s not in visited:
            visited[s] = dep

        if s in visited:
            if visited[s] > dep:
                visited[s] = dep

        for w in words:
            if CanChange(s,w):
                if w in visited:
                    if visited[w] > dep:
                        dfs(w,dep+1)

                elif w not in visited:
                    dfs(w,dep+1)

    dfs(begin,0)
    return min(answers)