# pd_code_reverse_component
reverse all arc number in one certain component for a link pd_code.

## Install

```bash
pip install pd-code-reverse-component
```

## Usage

```python
import pd_code_reverse_component

pd_code = [[8,11,9,12],[12,9,13,10],[10,13,11,14],[7,14,8,1],[4,1,5,2],[2,5,3,6],[6,3,7,4]]
print(reverse_component(pd_code, 1)) # reverse the component with arc 1
```
