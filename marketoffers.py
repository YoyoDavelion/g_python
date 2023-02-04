class HMarketPlaceOffer{
  offerId;
  status;
  furniType;
  furniId;
  stuffCategory;
  stuffData = null;
  extraData = "";
  uniqueSerialNumber = 0;
  uniqueSeriesSize = 0;
  price;
  timeLeftMinutes;
  averagePrice;
  offerCount;

  constructor(packet) {
    this.offerId = packet.readInteger();
    this.status = packet.readInteger();
    this.furniType = packet.readInteger();
    switch(this.furniType) {
      case 1:
        this.furniId = packet.readInteger();
        this.stuffCategory = packet.readInteger();
        this.stuffData = HStuff.readData(packet, this.stuffCategory);
        break;
      case 2:
        this.furniId = packet.readInteger();
        this.extraData = packet.readString();
        break;
      case 3:
        this.furniId = packet.readInteger();
        this.uniqueSerialNumber = packet.readInteger();
        this.uniqueSeriesSize = packet.readInteger();
        break;
    }
    this.price = packet.readInteger();
    this.timeLeftMinutes = packet.readInteger();
    this.averagePrice = packet.readInteger();
    this.offerCount = packet.readInteger();
  }
  
  static parse(packet) {
    let offerCount = packet.readInteger();
    let offers = [];
    for(let i = 0; i < offerCount; i++) {
      offers.push(new HMarketPlaceOffer(packet));
    }
    return offers;
  }
} 
