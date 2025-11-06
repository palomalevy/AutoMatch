import placeholder from "../assets/logos/placeholder.png";

import acura from "../assets/logos/acura.png";
import alfa from "../assets/logos/alfa-romeo.png";
import aston from "../assets/logos/aston-martin.png";
import audi from "../assets/logos/audi.png";
import bmw from "../assets/logos/bmw.png";
import buick from "../assets/logos/buick.png";
import cadillac from "../assets/logos/cadillac.png";
import chevrolet from "../assets/logos/chevrolet.png";
import chrysler from "../assets/logos/chrysler.png";
import datsun from "../assets/logos/datsun.png";
import dodge from "../assets/logos/dodge.png";
import ferrari from "../assets/logos/ferrari.png";
import fiat from "../assets/logos/fiat.png";
import ford from "../assets/logos/ford.png";
import gmc from "../assets/logos/gmc.png";
import harley from "../assets/logos/harley-davidson.png";
import honda from "../assets/logos/honda.png";
import hyundai from "../assets/logos/hyundai.png";
import infiniti from "../assets/logos/infiniti.png";
import jaguar from "../assets/logos/jaguar.png";
import jeep from "../assets/logos/jeep.png";
import kia from "../assets/logos/kia.png";
import landRover from "../assets/logos/land-rover.png";
import lexus from "../assets/logos/lexus.png";
import lincoln from "../assets/logos/lincoln.png";
import mazda from "../assets/logos/mazda.png";
import mercedes from "../assets/logos/mercedes-benz.png";
import mercury from "../assets/logos/mercury.png";
import mini from "../assets/logos/mini.png";
import mitsubishi from "../assets/logos/mitsubishi.png";
import morgan from "../assets/logos/morgan.png";
import nissan from "../assets/logos/nissan.png";
import pontiac from "../assets/logos/pontiac.png";
import porsche from "../assets/logos/porsche.png";
import ram from "../assets/logos/ram.png";
import rover from "../assets/logos/rover.png";
import saturn from "../assets/logos/saturn.png";
import subaru from "../assets/logos/subaru.png";
import tesla from "../assets/logos/tesla.png";
import toyota from "../assets/logos/toyota.png";
import volkswagen from "../assets/logos/volkswagen.png";
import volvo from "../assets/logos/volvo.png";

const brandLogos = {
  acura,
  "alfa-romeo": alfa,
  "aston-martin": aston,
  audi,
  bmw,
  buick,
  cadillac,
  chevrolet,
  chrysler,
  datsun,
  dodge,
  ferrari,
  fiat,
  ford,
  gmc,
  "harley-davidson": harley,
  honda,
  hyundai,
  infiniti,
  jaguar,
  jeep,
  kia,
  "land rover": landRover,
  lexus,
  lincoln,
  mazda,
  "mercedes-benz": mercedes,
  mercury,
  mini,
  mitsubishi,
  morgan,
  nissan,
  pontiac,
  porsche,
  ram,
  rover,
  saturn,
  subaru,
  tesla,
  toyota,
  volkswagen,
  volvo,
};

const getBrandLogo = (brand) => {
  if (!brand) return placeholder;
  return brandLogos[brand.toLowerCase()] || placeholder;
}

export default getBrandLogo;