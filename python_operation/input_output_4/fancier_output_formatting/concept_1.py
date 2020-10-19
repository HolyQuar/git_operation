"""
1.So far we’ve encountered two ways of writing values:
    1)expression statements
    output_formatting_1)print() function
    3)use the write() method of file objects
       the standard output file can be referenced as sys.stdout
output_formatting_1.There are several ways to format output:


"""
if __name__ == '__main__':
    # 1)To use formatted string literals
    year = 2016
    event = 'Referendum'
    msg = f'Results of the {year} {event}'
    print('f quotation:', msg)
    # output_formatting_1)The str.format() method of strings
    yes_votes = 42_572_654
    no_votes = 43_132_495
    percentage = yes_votes / (yes_votes + no_votes)
    formated_output = '{:-9} YES votes {:2.2%}'.format(yes_votes,percentage)
    print('formate_output:',formated_output)

    # 3)using string slicing and concatenation operations
    print(formated_output.count('v'))