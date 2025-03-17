public class PontoEscavacao {
    private int id;
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    private String tipo;
    public String getTipo() {
        return tipo;
    }
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public double getLatitude() {
        return latitude;
    }
    public void setLatitude(double latitude) {
        this.latitude = latitude;
    }
    private double latitude;
    private double longitude;
    public double getLongitude() {
        return longitude;
    }
    public void setLongitude(double longitude) {
        this.longitude = longitude;
    }
    private double altitude;
    public double getAltitude() {
        return altitude;
    }
    public void setAltitude(double altitude) {
        this.altitude = altitude;
    }
    private String descricao;
    public String getDescricao() {
        return descricao;
    }
    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
    private String dataDescoberta;
    public String getDataDescoberta() {
        return dataDescoberta;
    }
    public void setDataDescoberta(String dataDescoberta) {
        this.dataDescoberta = dataDescoberta;
    }
    private String responsavel;
    public String getResponsavel() {
        return responsavel;
    }
    public void setResponsavel(String responsavel) {
        this.responsavel = responsavel;
    }

    public PontoEscavacao(int id, String tipo, double latitude, double longitude, double altitude, String descricao, String datadescoberta, String responsavel){
        this.id = id;
        this.tipo = tipo;
        this.latitude = latitude;
        this.longitude = longitude;
        this.altitude = altitude;
        this.descricao = descricao;
        this.dataDescoberta = datadescoberta;
        this.responsavel = responsavel;
    }

    
}
