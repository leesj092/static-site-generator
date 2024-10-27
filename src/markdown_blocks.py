def markdown_to_blocks(markdown):
    splits = markdown.split('\n')
    blocks = []
    line = ''

    for i in range(len(splits) - 1):
        if splits[i] == '':
            continue

        if splits[i]:
            if line:
                line += '\n' + splits[i].strip()
            else:
                line = splits[i].strip()
        if not splits[i+1]:
            blocks.append(line)
            line = ''

    return blocks
