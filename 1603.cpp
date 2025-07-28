class ParkingSystem {
public:
    int bigs;
    int mediums;
    int smalls;

    ParkingSystem(int big, int medium, int small) {
        bigs = big;
        mediums = medium;
        smalls = small;
    }
    
    bool addCar(int carType) {
        if(carType == 3) {
            smalls--;
            if(smalls >= 0) {
                return true;
            }
        } else if(carType == 2) {
            mediums--;
            if(mediums >= 0) {
                return true;
            }
        } else if(carType == 1) {
            bigs--;
            if(bigs >= 0) {
                return true;
            }
        } else {
            return false;
        }

        return false;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */