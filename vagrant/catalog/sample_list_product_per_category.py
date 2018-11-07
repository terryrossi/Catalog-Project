cat = session.query(Category).all()
  for item in cat:
    print item.name
    prod = session.query(Product).join(Category).filter(Product.category_id==item.id).all()
    for itemprod in prod:
      print itemprod.name
     print "\n"
