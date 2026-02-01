// User function Template for C

/*
struct Complex
{
    int real;
    int img;
};
*/

struct Complex add(struct Complex c1, struct Complex c2) {

    // code here
    struct Complex res;
    res.real = c1.real + c2.real;
    res.img = c1.img + c2.img;
    return (res);
}