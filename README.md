# anzeige.py

A terminal markdown renderer using `ueberzug` to display images.

## Progress

- ☑️  Headers
- ☑️  Multiline code blocks
- ☑️  Scrolling
- ⬜️ Inline elements
- ⬜️ Displaying images
- ⬜️ Everything else

## Rendering Test 🧋
**bold text**
__bold 2
*italic text*
_italic 2
**nested bold and *italics***

A paragraph.

`Inline code`

```cpp
/**
 * Displays some text
 */
void Menu::DisplayText(std::string text = "Example code block") override {
    std::cout << text << std::endl;
}
```

```c#
public class CSharpCodeBlock {
    public string Example = "Example C#" { get; internal set; };
    public bool Example2 => Example != Function(this);
    public IInterface Function();
}
```

```
No language code block
```

## Dependencies
- `ueberzug` for displaying images
- `blessed` for rendering text
- `pygments` for syntax highlighting
- `click` for command-line arguments and options
