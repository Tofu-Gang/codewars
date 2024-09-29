"""
Text align justify
https://www.codewars.com/kata/537e18b6147aa838f600001b

Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the
expected justification width. The longest word will never be greater than this width.

Here are the rules:

-Use spaces to fill in the gaps between words.
-Each line should contain as many words as possible.
-Use '\n' to separate lines.
-Last line should not terminate in '\n'
-'\n' is not included in the length of a line.
-Gaps between words can't differ by more than one space.
-Lines should end with a word not a space.
-Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
-Last line should not be justified, use only one space between words.
-Lines with one word do not need gaps ('somelongword\n').

Example with width=30:

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.

Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align:
justify).

Have fun :)
"""


def justify(text: str, width: int) -> str:
    """
    Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and
    the expected justification width. The longest word will never be greater than this width.

    Here are the rules:
    -Use spaces to fill in the gaps between words.
    -Each line should contain as many words as possible.
    -Use '\n' to separate lines.
    -Last line should not terminate in '\n'
    -'\n' is not included in the length of a line.
    -Gaps between words can't differ by more than one space.
    -Lines should end with a word not a space.
    -Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
    -Last line should not be justified, use only one space between words.
    -Lines with one word do not need gaps ('somelongword\n').

    :param text: input text
    :param width: line length
    :return: input text separated into multiple lines, each line justified to exactly "width" characters
    """

    # first, separate the input text into lines
    lines = []
    for word in text.split():
        # get the last line created
        try:
            # no line yet, first word of the input
            line = lines[-1]
        except IndexError:
            # create list for the first line
            lines.append([])
            line = lines[-1]

        words_length = sum(len(word) for word in line)
        spaces_count = max(len(line) - 1, 0)
        if (words_length + spaces_count + len(word)) < width:
            # the word still fits into the line
            line.append(word)
        else:
            # the line would be too long, create another and start it with this word
            lines.append([word])

    # second, justify all the lines (except the last one)
    for i in range(len(lines) - 1):
        j = 0
        if len(lines[i]) > 1:
            # justify only lines with more than one word

            while sum(len(word) for word in lines[i]) < width:
                # add spaces to each word (except the last in line), starting from the first one until the line has
                # desired length
                lines[i][j] += " "
                if j < len(lines[i]) - 2:
                    j += 1
                else:
                    j = 0
    # all lines except for the last one are justified and the extra spaces are parts of word strings; those strings
    # will be created with no further separator
    # words in the last line must be separated with one space since this line is not justified and word strings do
    # not contain any spaces
    return "\n".join(" ".join(lines[i]) if i == len(lines) - 1 else "".join(lines[i]) for i in range(len(lines)))
