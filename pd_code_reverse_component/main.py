import pd_code_sanity
import pd_code_pre_nxt
import json

# 沿着 nxt 边走出一个 loop
def get_loop(nxt:dict, begin_val) -> list:
    loop = [begin_val]
    while True:
        loop.append(nxt[loop[-1]])
        if loop[-1] == loop[0]: # 如果第一个元素已经重复出现
            loop.pop()
            break
    return loop

# 翻转 val 所在的连通分支的所有编号
def reverse_component(pd_code:list[list], val):

    # 先备份
    pd_code = json.loads(json.dumps(pd_code))

    # 必须是合法 pd_code
    if not pd_code_sanity.sanity(pd_code):
        raise TypeError()
    
    # 没有出现过这个值，因此不能翻转
    if val not in set([
        term
        for crossing in pd_code
        for term in crossing
    ]):
        return pd_code
    
    # 计算前驱后继
    pre, nxt = pd_code_pre_nxt.get_pre_nxt(pd_code)

    # 先找到当前循环的最小元素
    min_val = min(get_loop(nxt, val))
    loop = get_loop(nxt, min_val) # 这样可以得到递增序列
    rev_loop = loop[::-1]         # 翻转的 list

    # 把出现过的值映射成大小相反的值
    num_map = {
        loop[i]: rev_loop[i]
        for i in range(len(loop))
    }

    # 编写针对一个对象的映射函数
    def map_one_data(term):
        if num_map.get(term) is None:
            return term
        else:
            return num_map[term]

    # 重新编码
    return [
        [map_one_data(term) for term in crossing]
        for crossing in pd_code
    ]

if __name__ == "__main__":
    pd_code = [[8,11,9,12],[12,9,13,10],[10,13,11,14],[7,14,8,1],[4,1,5,2],[2,5,3,6],[6,3,7,4]]
    print(reverse_component(pd_code, 1))
