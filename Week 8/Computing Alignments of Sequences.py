''' Week 4 Project '''


def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
  ''' 
  input: alphabet: set of characters, three scores(integer)
  output: dictionary of dictionaries whose entries are indexed by pairs of
  characters in alphabet plus -.
  '''

  scoring_matrix = {}
  scoring_matrix['-'] = {}

  #initialize an object for each letter
  for char1 in alphabet:
    scoring_matrix[char1] = {}
    scoring_matrix['-'][char1] = dash_score
    for char2 in alphabet:
      if char1 == char2:
        scoring_matrix[char1][char2] = diag_score
      else:
        scoring_matrix[char1][char2] = off_diag_score
    scoring_matrix[char1]['-'] = dash_score

  scoring_matrix['-']['-'] = dash_score

  return scoring_matrix


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
  '''
  Return an alignment matrix for two sequences(strings).
  If global flag is true: Compute global alignment matrix, otherwise
  local.
  '''

  alignment_matrix = []
  seq_x_length = len(seq_x)
  seq_y_length = len(seq_y)
  for row in range(0, seq_x_length + 1):
    current_row = []
    for col in range(0, seq_y_length + 1):
      current_row.append(0)
    alignment_matrix.append(current_row)

  for row in range(1, seq_x_length + 1):
    char = seq_x[row - 1]
    align_matrix_value = alignment_matrix[row -
                                          1][0] + scoring_matrix[char]['-']
    if align_matrix_value < 0 and not global_flag:
      alignment_matrix[row][0] = 0
    else:
      alignment_matrix[row][0] = alignment_matrix[row -
                                                  1][0] + scoring_matrix[char]['-']

  for col in range(1, seq_y_length + 1):
    char = seq_y[col - 1]
    align_matrix_value = alignment_matrix[0][col -
                                             1] + scoring_matrix[char]['-']
    if align_matrix_value < 0 and not global_flag:
      alignment_matrix[0][col] = 0
    else:
      alignment_matrix[0][col] = align_matrix_value

  for row in range(1, seq_x_length + 1):
    for col in range(1, seq_y_length + 1):
      char1 = seq_x[row - 1]
      char2 = seq_y[col - 1]
      align_matrix_value = max(scoring_matrix[char1][char2] + alignment_matrix[row - 1][col - 1], scoring_matrix['-'][char2] + alignment_matrix[row][col - 1],
                               scoring_matrix[char1]['-'] + alignment_matrix[row - 1][col])
      if align_matrix_value < 0 and not global_flag:
        alignment_matrix[row][col] = 0
      else:
        alignment_matrix[row][col] = align_matrix_value

  return alignment_matrix


def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
  '''
  Takes as input two sequences whose elements share a common alphabet, a scoring matrix and an alignment matrix.
  Returns a tuple of the form (score, align_x, align_y) where score is the max score in that alignment,
  and align_x and align_y are the aligned sequences in string form
  '''

  row_pointer = len(seq_x)
  col_pointer = len(seq_y)
  aligned_seq_x = ''
  aligned_seq_y = ''

  while row_pointer > 0 and col_pointer > 0:
    char_x = seq_x[row_pointer - 1]
    char_y = seq_y[col_pointer - 1]

    if alignment_matrix[row_pointer][col_pointer] == (alignment_matrix[row_pointer - 1][col_pointer - 1] + scoring_matrix[char_x][char_y]):
      aligned_seq_x = char_x + aligned_seq_x
      aligned_seq_y = char_y + aligned_seq_y
      row_pointer = row_pointer - 1
      col_pointer = col_pointer - 1
    elif alignment_matrix[row_pointer][col_pointer] == (alignment_matrix[row_pointer - 1][col_pointer] + scoring_matrix[char_x]['-']):
      aligned_seq_x = char_x + aligned_seq_x
      aligned_seq_y = '-' + aligned_seq_y
      row_pointer = row_pointer - 1
    else:
      aligned_seq_x = '-' + aligned_seq_x
      aligned_seq_y = char_y + aligned_seq_y
      col_pointer = col_pointer - 1
  while row_pointer > 0:
    aligned_seq_x = seq_x[row_pointer - 1] + aligned_seq_x
    aligned_seq_y = '-' + aligned_seq_y
    row_pointer = row_pointer - 1
  while col_pointer > 0:
    aligned_seq_x = '-' + aligned_seq_x
    aligned_seq_y = seq_y[col_pointer - 1] + aligned_seq_y
    col_pointer = col_pointer - 1

  return (alignment_matrix[len(seq_x)][len(seq_y)], aligned_seq_x, aligned_seq_y)


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
  '''
  Local version of compute global alignment.
  '''

  max_score = 0
  row_pointer = 0
  col_pointer = 0
  aligned_seq_x = ''
  aligned_seq_y = ''

  for row in range(0, len(alignment_matrix)):
    for col in range(0, len(alignment_matrix[0])):
      if alignment_matrix[row][col] > max_score:
        max_score = alignment_matrix[row][col]
        row_pointer = row
        col_pointer = col

  while alignment_matrix[row_pointer][col_pointer] > 0:
    char_x = seq_x[row_pointer - 1]
    char_y = seq_y[col_pointer - 1]

    print char_x, char_y

    if alignment_matrix[row_pointer][col_pointer] == alignment_matrix[row_pointer - 1][col_pointer - 1] + scoring_matrix[char_x][char_y]:
      aligned_seq_x = char_x + aligned_seq_x
      aligned_seq_y = char_y + aligned_seq_y
      row_pointer = row_pointer - 1
      col_pointer = col_pointer - 1
    elif alignment_matrix[row_pointer][col_pointer] == alignment_matrix[row_pointer - 1][col_pointer] + scoring_matrix[char_x]['-']:
      aligned_seq_x = char_x + aligned_seq_x
      aligned_seq_y = '-' + aligned_seq_y
      row_pointer = row_pointer - 1
    else:
      aligned_seq_x = '-' + aligned_seq_x
      aligned_seq_y = char_y + aligned_seq_y
      col_pointer = col_pointer - 1

  return (max_score, aligned_seq_x, aligned_seq_y)
