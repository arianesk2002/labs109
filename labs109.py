#N_1
def count_troikas(items):
    troika_counter = 0
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            k = 2 * j - i
            if k < len(items) and items[i] == items[j] == items[k]:
                troika_counter += 1
    return troika_counter

#N_2
def is_integer1(number):
    if type(number) == int or str(number).split('.')[1] == '0':
      return True
    return False
  
def collatz(number):
    shapes = ''
    while number > 1:
        if number % 2 == 0:
          number /= 2
          shapes += 'd'
        else:
          number = (number * 3) + 1
          shapes += 'u'
    return shapes

def ztalloc(shape):
    inverse_shape_list = []
    for i in range(len(shape) - 1, -1, -1):
      inverse_shape_list.append(shape[i])

    goal_state = 1
    for letter in inverse_shape_list:
      if is_integer1(goal_state):
        if letter == 'd':
          goal_state *= 2
        else:
          goal_state = (goal_state - 1) / 3
      else:
        return None
    
    if is_integer1(goal_state) and collatz(goal_state) == shape:
        return int(goal_state)
    else:
        return None

#N_3
def is_cyclops(n):
    digits=str(n)
    if len(digits)%2==0:
        return False
    elif len(digits)%2!=0:
        middle_number=len(digits)//2
        if digits[middle_number]!='0':
            return False
        cnt = 0
        for i in digits:
            if i == '0':
                cnt += 1
        if cnt>1:
            return False
        return True
    
#N_4
def calkin_wilf(n):
    Up, Down = 1, 1
    # Up = Nominator
    #Down = Denominator
    
    cnt = 1

    while True:
        
        Up, Down = Down, Up - 2 * (Up % Down) + Down
        
        cnt += 1
        
        if cnt == n:
            if Down != 1:
                return str(Up) + '/' + str(Down)
            else: # if not Fractional
                return str(Up)
    
#N_5
def josephus(n, k):
    l1 = list(range(1, n + 1))
    ans = []
    i = 0
    while len(l1) > 0:
        i = (i + k - 1) % len(l1)
        ans.append(l1[i])
        del l1[i]
    return ans

#N_6
def can_balance(items):
    
    if len(items)==1:
        return 0
    
    po = False # Detrmine to move Right or Left
    
    x = int(len(items) / 2) #for Optimize  
    
    while x < len(items) and x >= 0:
        l = 0
        r = 0
        
        #Right Weight
        for j in range(x+1, len(items)):
            r += (abs(j - x) * items[j])
        
        #Left Weight
        for j in range(x - 1, -1, -1):
            l += (abs(x - j) * items[j])   
        
        if l == r:
            return x
        elif l < r and not po:
            determined = 1
            po = True
        elif l > r and not po:
            determined = -1
            po = True
        x += determined
    return -1
 
#N_7
def group_and_skip(n, out, ins):
    l1 = []
    while (piles:= n // out) > 0:
        l1.append(n % out)
        n = ins * piles
    else:
        l1.append(n % out)
    return l1



#N_8
def eliminate_neighbours(items):
    n = len(items) #The length of the list
    step = 0
    
    #step count
    for i in range(1, len(items) + 1):
        if i in items:
            step += 1
            
            #if it's the last step
            if len(items) == 1:
                items.pop(0)
                break
            
            org = items.index(i) #find index
            left = org - 1
            right = org + 1
            
            #find the larger element(value)
            if left < 0 or (right < len(items) and items[right] > items[left]):
                left = right
            value = items[left]
            
            #remove two element
            if org > left:
                org = left
            items.pop(org)
            items.pop(org)
            
            if value == n: # if value == max
                break
            
    return step


#N_9
def lunar_add(a, b): #max
    #convert to string and reverse it
    a_str_r, b_str_r = str(a)[::-1], str(b)[::-1]
    sum = ''
    #detection of the maximum length of the number and maximum calculation(sum)
    for i in range(max(len(a_str_r), len(b_str_r))):
        sum += max(a_str_r[i:i+1], b_str_r[i:i+1])
        
    return int(sum[::-1])

def lunar_multiply(a, b): #min
    #convert to string and reverse it
    a_str_r, b_str_r = str(a)[::-1], str(b)[::-1]
    
    numbers = [] #to save the numbers that obtained
    answer = 0 
    
    #minimum calculation(sum)
    for i in range(len(b_str_r)):
        d = ''
        for j in range(len(a_str_r)):
            d += min(a_str_r[j], b_str_r[i])
        #This zero is added because at each step in normal multiplication when we go down, we add a zero to the end of the number and add it at the end, and since our number is reversed, we add this zero to the beginning of it.
        numbers.append('0' * i + d) 
    #Here we add the numbers of each step(for multi-digit numbers)
    for i in numbers:
        answer = lunar_add(answer, i[::-1])
    return answer
#N_10
def is_chess_960(row):
    # Check "K" condition
    r1 = row.find("r")
    s_new = row[r1+1:]
    r2 = s_new.find("r")
    r2 += r1 + 1
    x = row.find("K")
    
    if not(x > r1 and x < r2):
        return False
    
    # Check "b" condition
    b1 = row.find("b")
    s_new = row[b1+1:]
    b2 = s_new.find("b")
    b2 += b1 + 1
    if (b2 - b1) % 2 != 1:
        return False
    
    return True

#N_11
def multiplicative_persistence(n, ignore_zeros=False):
    step = 0 #count step
    str_n = str(n) # convert to string for Access to numbers
    
    while len(str_n) > 1:
        b = 1
        for i in str_n:
            if ignore_zeros == False:
                b *= int(i)
            else:
                if int(i) == 0:
                    continue
                else:
                    b *= int(i)
        step += 1
        str_n = str(b)
    
    return step

#N_12
def costas_array(rows):
    n = len(rows)
    dvs = set()  
    placed = dict()  
    to_fill = [row for (row, col) in enumerate(rows) if col is None]  
    still_free = [True for _ in range(n)]  

    def place_rook(row, col, undo_stack=None):
        for prev_row in placed:
            prev_col = placed[prev_row]
            dx, dy = row - prev_row, col - prev_col
            if (dx, dy) in dvs or (-dx, -dy) in dvs:
                return False
            dvs.add((dx, dy))
            if undo_stack is not None:
                undo_stack.append((dx, dy))

        placed[row] = col
        still_free[col] = False
        return True

    for (row, col) in enumerate(rows):
        if col is not None:
            if not place_rook(row, col):
                return False

    def fill_remaining():
        if len(to_fill) == 0:
            return True

        row = to_fill.pop()
        undo_stack = []
        for col in range(n):
            if still_free[col]:
                if place_rook(row, col, undo_stack):
                    if fill_remaining():
                        return True

                    still_free[col] = True
                    del placed[row]

                while len(undo_stack) > 0:
                    dvs.remove(undo_stack.pop())

        to_fill.append(row)
        return False

    return fill_remaining()