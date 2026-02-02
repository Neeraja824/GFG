double posAverage(int numbers[], int size) {
    int count = 0;
    int sum = 0;
    for(int i=0;i<size;i++){
        if(numbers[i] >= 0){
            count++;
            sum += numbers[i];
        }
    }
    return (sum*(1.0))/count;
}