from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'one_app/index.html')

one_digits ={
    1: "one", 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight',
    9: 'nine'
}

firs_tens ={
    10:'ten', 11:'eleven', 12: 'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
    16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'
}


sec_tens = {
    2:'twenty-', 3:'thirty-', 4:'forty-', 5:'fifty-', 6:'sixty-', 7:'Seventy-',
    8:'eighty-', 9:'ninety-'
}


def num_to_str(num):
    '''
    Create a function that turns a user input into the string version
    '''
    tens_digit = num//10
    firs_digit = num%10
    
    if tens_digit == 0:
        return one_digits[num]
    elif tens_digit == 1:
        return firs_tens[num]
    
    elif 2<= tens_digit <= 9:
        if firs_digit ==0:
            return sec_tens[num] 
        elif 1<= firs_digit <= 9:
            new_str = sec_tens[tens_digit] + one_digits[firs_digit]

            return new_str
    

def result(request):
    if request.method == 'GET':
        
        return render(request, 'one_app/index.html')
    
    elif request.method == 'POST':
        print(request.POST['number'])

        user = request.POST['number']
        num = int(user)
        result_value = num_to_str(num) 

        return render(request, 'one_app/result.html', { 'result_value':result_value

        })
