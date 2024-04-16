from clpg285b import salespersom


def main():
  try
    print("Number\tCode\tSales\tComission")
    with open ("Langdat\prog285b.dat", 'r')
      for line in f:
        Idata = line.split(" ")
        id = int(idata[0])
        code = int(Idata[1])
        sales = float(Idata[2])
      seller = salespersom(id, code, sales)
      seller.setComm()
      print(str(seller))

    except Exception as e:
      print("Error", e)



if __name__ == "__main__":
  main()
