# pd-code-reverse-component

Reverse the orientation encoding of one selected PD-code component.

## Installation

```bash
pip install pd-code-reverse-component
```

## Usage example

```python
from pd_code_reverse_component import reverse_component

pd = [[2, 3, 1, 4], [4, 1, 3, 2]]
reversed_pd = reverse_component(pd, 1)
print(reversed_pd)
```

## Algorithm

The selected label identifies its component cycle through predecessor/successor maps. The cycle is placed in canonical order and mapped to its reverse order. Every occurrence of a component label is replaced through that bijection; labels belonging to other components remain unchanged. The operation returns a deep copy and leaves the input untouched. If the selected label is absent, the unchanged deep copy is returned.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

No external software is required.

## Development

Python 3.10 or newer is required. Run tests with the two declared PD-code
dependencies available:

```bash
python -m unittest discover -s tests -v
```

No PyPI publication is performed as part of repository maintenance.

## License

MIT. See `LICENSE`.
