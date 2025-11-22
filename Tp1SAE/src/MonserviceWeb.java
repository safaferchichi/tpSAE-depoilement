import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;

@WebService(targetNamespace = "https://www.galille.fr/")
public class MonserviceWeb {

    @WebMethod(operationName = "convertir")
    public double conversion (double mt) {
        return mt*0.9;
    }
    public double somme (@WebParam(name="param 1") double a , double b) {
        return a+b;
    }
    public Etudiant getEtudiant(int identifiant) {
        return new Etudiant (  1, "Mario",  19);
    }
}
