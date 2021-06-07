# Parser Breakdown

The source document will go through several filters which will create elements
based on regular expression.

The current process for generating these elements is:

```
source document -> generate block elements (headers, code blocks, paragraphs,
tables, etc.) -> generate inline elements in paragraphs (bold, italics, etc.)
-> filter paragraphs
```

After parsing, the renderer writes text based on the elements created from the
parser.
