# cpp_gui_juce

This is where your JUCE project lives. Use Projucer to create a new GUI application,
then in your processor, call the `generate_notes` function from the Rust shared library.

Example C++:
```cpp
extern "C" float generate_notes(const float* input_ptr, size_t len);
```
