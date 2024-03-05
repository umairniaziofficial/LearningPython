def Merger_Sort(arr):
    if len(arr)>1:
        array_mid = len(arr)//2
        Left,Rigt = arr[:array_mid],arr[array_mid:]
        Merger_Sort(Left)
        Merger_Sort(Rigt)
        arr[:] = sorted(Left + Rigt)

def Print_Array(arr):
    print(" ".join(map(str,arr)))
    

choice = int(input("[*] Want to Sort Custon Array Press 1\n[*] Sort The Predefined Array Press 2\n[*] Exit\n"))
demoArray = [9,3,1,51,2]
if choice == 1:
    Merger_Sort(demoArray)
    Print_Array(demoArray)
elif choice ==2:
    input_str = input("Enter elements of the array separated by space: ")
    arr = list(map(int, input_str.split()))
    Merger_Sort(arr)
    Print_Array(arr)
else:
    print("invalid choice Exiting!")

    