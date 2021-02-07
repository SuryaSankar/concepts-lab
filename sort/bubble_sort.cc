#include <vector>

using std::vector;

vector<int> BubbleSort(vector<int> lst){
    for(int endPtr=lst.size() - 1; endPtr >= 0; endPtr--){
        for(int i=0; i<endPtr; i++){
            if(lst[i] > lst[i+1]){
                int temp = lst[i];
                lst[i] = lst[i+1];
                lst[i+1] = temp;
            }
        }
    }
    return lst;
}

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
