import os

def read_files(file_names):
    file_contents = {}
    for file_name in file_names:
        with open(file_name, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            file_contents[line_count] = [f"{file_name}\n", f"{line_count}\n"] + lines
    return file_contents


def write_sorted_content(file_contents, output_file):
    sorted_file_contents = dict(sorted(file_contents.items()))
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for content in sorted_file_contents.values():
            result_file.writelines(content)
            result_file.write('\n')


def main():
    file_names = [f for f in os.listdir('.') if f.endswith('.txt')]
    file_contents = read_files(file_names)
    write_sorted_content(file_contents, 'result.txt')


if __name__ == "__main__":
    main()
