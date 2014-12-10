#include <stdio.h>
#include <stdlib.h>

int fib       (int first, int second, int count, int *sequence);
int fib_rec   (int first, int second, int count, int *target);
int fib_print (int first, int second, int count);

int main (int argc, char* argv[]) {
  int count, first, second;
  count = 10;
  first = 1;
  second = 1;
  
  switch (argc) {
    case 2:
      count = atoi(argv[1]);
      break;
    case 3:
      count = atoi(argv[1]);
      first = atoi(argv[2]);
      second = atoi(argv[2]);
      break;
    case 4:
      count = atoi(argv[1]);
      first = atoi(argv[2]);
      second = atoi(argv[3]);
      break;
    default:
      break;
  }

  fib_print(first, second, count);

  return 0;
}


int fib(int first, int second, int count, int *sequence) {
  sequence[0] = first;
  sequence[1] = second;
    
  return fib_rec(first, second, count - 2, sequence + 2);
}

int fib_rec(int first, int second, int count, int *target) {
  if (count <= 0)
    return 0;

  *target = first + second;
  return fib_rec(second, *target, count - 1, target + 1);
}

int fib_print (int first, int second, int count) {
  int* sequence = malloc(count * sizeof(int));
    
  fib(first, second, count, sequence);
  int i;
  for (i = 0; i < count; ++i) {
    printf("%i\n", sequence[i]);
  }

  free(sequence);

  return 0;
}
