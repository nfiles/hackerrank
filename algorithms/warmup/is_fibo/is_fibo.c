#include <stdio.h>
#include <stdlib.h>

int fib       (int first, int second, int count, int *sequence);
int fib_rec   (int first, int second, int count, int *target);

int main() {

  int fibonacci_length = 100;
  int* fibonacci = malloc(fibonacci_length * sizeof(int));
  fib(0, 1, fibonacci_length, fibonacci);

  int T, N, is_fibo;

  scanf("%i", &T);
  for(int i = 0; i < T; ++i) {
    scanf("%i", &N);

    is_fibo = 0;
    for (int j = 0; j < fibonacci_length; ++j) {
      if (fibonacci[j] == N) {
	is_fibo = 1;
	break;
      }
    }

    if (is_fibo == 1) {
      printf("IsFibo\n");
    } else {
      printf("IsNotFibo\n");
    }
  }

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
