#### 1
## 5

#### 2
## 1080

#### 3
## 26

#### 4
## 2048

#### 5
## 12

#### 6
## 4

#### 7
## x

#### 8
## 23

#### 9
## 19

#### 10
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2)
    else:
        return 1 + f(n - 1)


counter = 0
for n in range(1, 501):
    if f(n) == 3:
        counter += 1
print(counter)
## 84

#### 11
f = (4 ** 36) + 3 * (4 ** 20) + (4 ** 15) + 2 * (4 ** 7) + 49
hexf = hex(f)
print(hexf)
## 5





############################# last dz ################
#### 1                      #### 8
## 16                       ## 151

#### 2                      #### 9
## 4                        ## 45

#### 3                      #### 10
## 21102                    ## 35

#### 4                      #### 11
## 26                       ## 3

#### 5                      #### 12
## 88                       ## 112

#### 6                      #### 13
## 512                      ## 18

#### 7                      #### 14
## 36                       ## 32



















