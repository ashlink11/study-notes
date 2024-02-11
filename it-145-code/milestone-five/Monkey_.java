/**
 * Monkey class, which inherits from RescueAnimal
 * 
 * has 2 constructors: 
 * 1. default constructor (no params) 
 * 2. full constructor (13 params)
 * 
 * total of 13 member variables: 
 * - inherits 9 attributes & their getters/setters
 * - creates 4 attributes & their getters/setters
 */
public class Monkey extends RescueAnimal {

	// Monkey-specific private member variables which
	// are not from the RescueAnimal class.
	// 
	// Uses String for all fields which follows the
	// conventions in the Dog.java file.
	private String species;
	private String tailLength;
	private String height;
	private String bodyLength;

	/**
	 * default Monkey constructor
	 * 
	 * default values: 
	 * - String: null 
	 * - boolean: false
	 */
	public Monkey() {
		// set attributes inherited from RescueAnimal
		setName(null);
		setGender(null);
		setAge(null);
		setWeight(null);
		setAcquisitionDate(null);
		setAcquisitionLocation(null);
		setTrainingStatus(null);
		setReserved(false);
		setInServiceCountry(null);

		// set Monkey-specific attributes
		setSpecies(null);
		setTailLength(null);
		setHeight(null);
		setBodyLength(null);
	}

	/**
	 * Monkey constructor with 13 parameters, which sets all possible member
	 * variables to the 13 arguments inputted
	 */
	public Monkey(String name, String gender, String age, String weight, 
			String acquisitionDate, String acquisitionCountry, String trainingStatus, 
			boolean reserved, String inServiceCountry, String species,
			String tailLength, String height, String bodyLength) {

		// set attributes inherited from RescueAnimal
		setName(name);
		setGender(gender);
		setAge(age);
		setWeight(weight);
		setAcquisitionDate(acquisitionDate);
		setAcquisitionLocation(acquisitionCountry);
		setTrainingStatus(trainingStatus);
		setReserved(reserved);
		setInServiceCountry(inServiceCountry);

		// set Monkey-specific attributes
		setSpecies(species);
		setTailLength(tailLength);
		setHeight(height);
		setBodyLength(bodyLength);

	}

	/**
	 * four sets of Monkey-specific getter/setter method pairs
	 */

	// 'species' getter/setter pair

	public String getSpecies() {
		return this.species;
	}

	public void setSpecies(String species) {
		this.species = species;
	}

	// 'tailLength' getter/setter pair

	public String getTailLength() {
		return this.tailLength;
	}

	public void setTailLength(String tailLength) {
		this.tailLength = tailLength;
	}

	// 'height' getter/setter pair

	public String getHeight() {
		return this.height;
	}

	public void setHeight(String height) {
		this.height = height;
	}

	// 'bodyLength' getter/setter pair

	public String getBodyLength() {
		return this.bodyLength;
	}

	public void setBodyLength(String bodyLength) {
		this.bodyLength = bodyLength;
	}

}