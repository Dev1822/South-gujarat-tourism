import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()
window.title("Hidden Gems of Gujarat")
window.config(bg="#001f3d")
window.geometry("1920x1080")

places = {
    "Tithal Beach": """Tithal Beach is a beach along the Arabian Sea located 4 km west of Valsad town.
    This beach is famous for its black sand. It is a popular touristdestination of Valsad.
    Apart from the beach, places of interest at Tithal including two major temples- the Shri Sai Baba temple located 1.5 km south ofthe main beach and Shri Swami Narayan temple located 1.6 km north of themain beach. 
    Both the temples overlook the Arabian Sea.""",
    "Tadkeshwar Mahadev Temple": """It is a renowned temple in the town of Valsad, the Tadkeshwar Mahadev Temple is famous for the Various types of Shivling. 
    Since there is no ceiling and the sun shines over the Shivlings continuously, the name Tadkeshwar is given to the temple (where tadko-is sunlight Gujarat language). 
    It’s called as Tadkeshwar because there is no roof and heard that constant sunlight should touch the Shivling.""",
    "Parnera Hill": """Parnera hill is famous because of the historical temples. 
    It have the temple of Lord Shiva and Goddess Ambica, Chandica, Navdurga and Goddess Kalika and Parnera.
    Many Devotees arrive on aatham to get blessings from Mataji on the 8th day of Navratri. 
    Each year, on the Parnera Hill, Local Mela is hosted in the month of October. It is 5 km away from valsad city.""",
    "Wilson Hills": """Wilson Hills is a hill station in the Indian state of Gujarat. It is near Dharampur Taluka and is also the nearest hill station to Surat. 
    Presently Tourism Department is thinking of a development project here too. 
    If you come in summer you will enjoy cool weather & famous local mangoes.Wilson Hills stands in a densely forested region close to the Pangarbari Wildlife Sanctuary. 
    It is one of the few hill stations in the world from which it is possible to glimpse the sea.It has an average elevation of 750m (2500 feet). 
    The Wilson Hills are popular during the summer months as it enjoys a cooler and less humid climate than the surrounding area.This station is 27 Kms away from Dharampur city. 
    The famous “chhatri” made of marbles is the prime attraction of this place. It is one of the best sites for people who are interested in activities like Trekking.""",
}
placesn= {
    "Dandi Beach": """Dandi Beach is a serene coastal destination located along the Arabian Sea, known for its tranquil atmosphere and breathtaking scenic beauty. 
    This beach holds historical significance as the site where Mahatma Gandhi launched the Salt March in 1930, making it a landmark of India's freedom struggle. 
    The beach features soft sands, gentle waves, and beautiful palm trees, making it perfect for relaxation, leisurely beach walks, and enjoying stunning sunsets. 
    Visitors can also engage in various water sports and activities, making it a great spot for families and groups looking to spend quality time together.""",
    "Andheshwar Mahadev Temple": """Andheshwar Mahadev Temple is a revered temple dedicated to Lord Shiva, renowned for its unique architecture and tranquil surroundings. 
    This sacred site attracts devotees and tourists alike, who come to seek blessings and participate in the daily rituals conducted by the priests. 
    The temple is adorned with beautiful carvings and sculptures, creating a serene environment for meditation and reflection. 
    The annual festivals celebrated here draw large crowds, making it an essential part of the spiritual landscape in Navsari.""",
    "Funkiddo": """Funkiddo is an exciting amusement park situated in Navsari, designed to offer a wide range of rides and attractions that cater to children and families. 
    The park is filled with colorful rides, fun games, and entertaining activities, making it an ideal place for a day filled with laughter and joy. 
    From thrilling roller coasters to gentle rides for younger children, Funkiddo ensures that visitors of all ages have an enjoyable experience. 
    Families can spend a full day here, with plenty of food stalls and rest areas available to enhance their visit.""",
    "Unai Mata Temple": """Unai Mata Temple is a prominent pilgrimage site dedicated to the goddess Unai Mata, nestled in a picturesque setting surrounded by lush greenery. 
    This temple is known for its spiritual significance and attracts many devotees throughout the year. 
    The temple features exquisite architecture and is often visited during the Navratri festival, when special events and rituals are held to honor the goddess. 
    Devotees come here to seek blessings and participate in various ceremonies, making it a vibrant center of faith and devotion in the region. 
    The atmosphere is filled with devotion, especially during festivals, creating a unique and uplifting experience for visitors.""",
}
placesd= {
    "Saputara Lake": """Saputara Lake is a picturesque man-made reservoir nestled amidst the Sahyadri Mountains in Gujarat, India. 
    Surrounded by lush greenery and offering breathtaking views, the lake is a popular tourist destination for boating, picnicking, and nature walks. 
    The serene atmosphere and tranquil waters create a perfect escape from the hustle and bustle of city life.""",
    "Gira Falls": """Gira Falls is a picturesque waterfall located in the Dang district of Gujarat, India. It is a popular tourist destination known for its stunning beauty and natural surroundings. 
    The falls are surrounded by lush green forests and offer a peaceful and serene atmosphere. 
    Visitors can enjoy the scenic beauty of the waterfall, take a refreshing dip in the natural pool at the base, or simply relax and enjoy the tranquility of the area.""",
    "Saputara Tribal Museum": """Saputara Tribal Museum is a fascinating museum located in Saputara, Gujarat, India. 
    It showcases the rich cultural heritage of the region's tribal communities, featuring traditional artifacts, textiles, jewelry, and historical photographs. 
    Visitors can learn about the diverse cultures and traditions of the tribal people in Saputara.""",
    "Waghai Botanical Garden": """Waghai Botanical Garden is a serene botanical garden located in the Waghai forest range of Dang district, Gujarat. 
    It features a diverse collection of plants, including medicinal herbs and rare orchids. 
    Visitors can explore the garden, learn about the plants, and enjoy the peaceful atmosphere of the forest. 
    The garden is a great destination for nature lovers and those seeking a tranquil retreat.""",
}
placess= {
    "Galteshwar": """Galteshwar is a beautiful Hindu temple dedicated to Lord Shiva, located in Surat, Gujarat. 
    It is a popular pilgrimage site, especially during the monsoon season. The temple is known for its intricate architecture and peaceful atmosphere. 
    Visitors can enjoy the scenic beauty of the nearby Tapi River and indulge in delicious local cuisine.""",
    "Gopi Talav": """Gopi Talav is a beautiful man-made lake located in Surat, Gujarat, India. It is a popular spot for picnics, boating, and enjoying the scenic beauty of the surrounding area. 
    The lake is surrounded by lush greenery and offers a peaceful atmosphere. 
    Visitors can also enjoy various water sports activities and explore the nearby attractions in Surat.""",
    "VR Surat": """VR Surat is a popular shopping mall in Surat, Gujarat, offering a wide range of premium brands, a food court, a multiplex cinema, and a gaming zone. 
    It's a great destination for shopping, dining, and entertainment.""",
    "Sarthana Nature Park": """Sarthana Nature Park is a beautiful urban park in Surat, Gujarat. 
    It's home to a variety of flora and fauna, including butterflies. Visitors can enjoy leisurely walks, relax, or have picnics. 
    One highlight is the butterfly garden, where visitors can observe these beautiful creatures up close.""",
}
v=open("Valsad.dat","wb")
pickle.dump(places,v)
v.close()
n=open("Navsari.dat","wb")
pickle.dump(placesn,n)
n.close()
s=open("Surat.dat","wb")
pickle.dump(placess,s)
s.close()
d=open("Dang.dat","wb")
pickle.dump(placesd,d)
d.close()
def load(): # Clear any existing widgets in the window
    global vr,nr,sr,dr
    v=open("valsad.dat","rb+")
    try:
        while True:
            vr=pickle.load(v)
    except EOFError:
        v.close()
    n=open("navsari.dat","rb+")
    try:
        while True:
            nr=pickle.load(n)
    except EOFError:
        n.close()
    s=open("surat.dat","rb+")
    try:
        while True:
            sr=pickle.load(s)
    except EOFError:
        s.close()
    d=open("dang.dat","rb+")
    try:
        while True:
            dr=pickle.load(d)
    except EOFError:
        d.close()


def clear_widgets():
    for widget in window.winfo_children():
        widget.destroy()

file_names = {
    "Valsad": "valsad.dat",
    "Dang": "dang.dat",
    "Navsari": "navsari.dat",
    "Surat": "surat.dat"
}

def placea(place):
    clear_widgets()
    frameva = tk.Frame(window, bg="#001f3d")
    frameva.pack(expand=True)
    x = file_names[place]

    def insertv():
        clear_widgets()
        framevai = tk.Frame(window, bg="#001f3d")
        framevai.pack(expand=True)
        
        pv = tk.Label(framevai, text="Place You Want To Add", bg="#001f3d", fg="#ffd700")
        pv.grid(row=0, column=0, padx=10, pady=10)
        iv = tk.Label(framevai, text="Place Description", bg="#001f3d", fg="#ffd700")
        iv.grid(row=0, column=1, padx=10, pady=10)

        pve = tk.Entry(framevai, width=30)
        pve.grid(row=1, column=0, padx=10, pady=10)
        ive = tk.Entry(framevai, width=30)
        ive.grid(row=1, column=1, padx=10, pady=10)

        # Function to save data
        def save_data():
            place_name = pve.get().strip()
            description = ive.get().strip()

            load()
            
            if place_name and description:  # Check for non-empty fields
                try:
                    # Open file in read-binary mode to check for existing places
                    fva = open(x, "rb")
                    existing_places = pickle.load(fva)
                    fva.close()

                    # Check if the place already exists 
                    if any(key.lower() == place_name.lower() for key in existing_places.keys()):
                        tkinter.messagebox.showerror(title="Error", message="Place already exists!")
                        return  # Exit the function if the place exists

                    # If it doesn't exist, open file in append-binary mode
                    fva = open(x, "rb+")
                    existing_places[place_name] = description
                    fva.seek(0)  # Move the pointer to the beginning of the file
                    pickle.dump(existing_places, fva)
                    fva.truncate()  # Truncate the file to the new size
                    fva.close()

                    # Clear input fields
                    pve.delete(0, tk.END)
                    ive.delete(0, tk.END)
                except Exception as e:
                    print(f"Error saving data: {e}")

        save_button = tk.Button(framevai, text="Save Place", command=save_data, bg="#001f3d", fg="#ffd700", font=("Arial", 12))
        save_button.grid(row=2, column=0, padx=10, pady=10)
        back_button = tk.Button(framevai, text="Back", command=lambda: placea(place), bg="#001f3d", fg="#ffd700", font=("Arial", 12))
        back_button.grid(row=2, column=1, padx=10, pady=10)
   
    def search():       
        clear_widgets()
        framevas= tk.Frame(window, bg="#001f3d")
        framevas.pack(expand=True)

        load()
        
        pv = tk.Label(framevas, text="Place You Want To Search", bg="#001f3d", fg="#ffd700")
        pv.grid(row=0, column=0, padx=10, pady=10)
        pve = tk.Entry(framevas, width=30)
        pve.grid(row=0, column=1, padx=10, pady=10)

        def save_data():
            place_name = pve.get().strip().lower()  
            
            if place_name:  # Only search if the field is filled
                found = False
                try:
                    fva = open(x, "rb")
                    while True:
                        # Load each dictionary entry and check for the place name
                        data = pickle.load(fva)
                        
                        # Check if the place name exists
                        for key in data.keys():
                            if key.lower() == place_name:  
                                description = data[key]
                                tkinter.messagebox.showinfo(title=key, message=description)
                                found = True
                                break
                        if found:
                            break
                except EOFError:
                    if not found:
                        tkinter.messagebox.showinfo(title="Not Found", message="Place not found in records.")
                except FileNotFoundError:
                    tkinter.messagebox.showerror(title="File Error", message="Data file not found.")

        save_button = tk.Button(framevas, text="Search Place", command=save_data, bg="#001f3d", fg="#ffd700", font=("Arial", 12))
        save_button.grid(row=2, column=0, padx=10, pady=10)
        back_button = tk.Button(framevas, text="Back", command=lambda: placea(place), bg="#001f3d", fg="#ffd700", font=("Arial", 12))
        back_button.grid(row=2, column=1, padx=10, pady=10)

    def update():
        clear_widgets()
        framevau = tk.Frame(window, bg="#001f3d")
        framevau.pack(expand=True)
        
        pv = tk.Label(framevau, text="Place You Want To Update", bg="#001f3d", fg="#ffd700")
        pv.grid(row=0, column=0, padx=10, pady=10)
        iv = tk.Label(framevau, text="New Place Description", bg="#001f3d", fg="#ffd700")
        iv.grid(row=0, column=1, padx=10, pady=10)

        pve = tk.Entry(framevau, width=30)
        pve.grid(row=1, column=0, padx=10, pady=10)
        ive = tk.Entry(framevau, width=30)
        ive.grid(row=1, column=1, padx=10, pady=10)

        def save_data():
            place_name = pve.get().strip()
            new_description = ive.get().strip()
            
            if place_name and new_description:  # Only proceed if both fields are filled
                load()  # Load existing places
                
                try:
                    # Open file in read-binary mode to check for existing places
                    fva = open(x, "rb")
                    existing_places = pickle.load(fva)
                    fva.close()

                    # Check if the place exists
                    existing_keys = [key.lower() for key in existing_places.keys()]
                    if place_name.lower() not in existing_keys:
                        tkinter.messagebox.showerror(title="Error", message="Place does not exist!")
                        return  # Exit the function if the place does not exist

                    # If it exists, update the description
                    actual_key = next(key for key in existing_places.keys() if key.lower() == place_name.lower())
                    existing_places[actual_key] = new_description
                    fva = open(x, "wb")  # Open file in write-binary mode
                    pickle.dump(existing_places, fva)
                    fva.close()

                    # Clear input fields
                    pve.delete(0, tk.END)
                    ive.delete(0, tk.END)
                except Exception as e:
                    print(f"Error updating data: {e}")

        save_button = tk.Button(framevau, text="Update Place", command=save_data, bg="#001f3d", fg="#ffd700", font=("Arial", 12))
        save_button.grid(row=2, column=0, padx=10, pady=10)
        back_button = tk.Button(framevau, text="Back", command=lambda: placea(place), bg="#001f3d", fg="#ffd700", font=("Arial", 12))
        back_button.grid(row=2, column=1, padx=10, pady=10)

    def delete():
        clear_widgets()
        framevad = tk.Frame(window, bg="#001f3d")
        framevad.pack(expand=True)

        pv = tk.Label(framevad, text="Place You Want To Delete", bg="#001f3d", fg="#ffd700")
        pv.grid(row=0, column=0, padx=10, pady=10)

        pve = tk.Entry(framevad, width=30)
        pve.grid(row=0, column=1, padx=10, pady=10)

        def save_data():
            place_name = pve.get().strip()

            if place_name:  # Only proceed if the field is filled
                load()  # Load existing places
                
                try:
                    # Open file in read-binary mode to check for existing places
                    fva = open(x, "rb")
                    existing_places = pickle.load(fva)
                    fva.close()

                    # Check if the place exists 
                    existing_keys = [key.lower() for key in existing_places.keys()]
                    if place_name.lower() not in existing_keys:
                        tkinter.messagebox.showerror(title="Error", message="Place does not exist!")
                        return  # Exit the function if the place does not exist

                    # If it exists, delete the place
                    actual_key = next(key for key in existing_places.keys() if key.lower() == place_name.lower())
                    del existing_places[actual_key]
                    
                    fva = open(x, "wb")  # Open file in write-binary mode
                    pickle.dump(existing_places, fva)
                    fva.close()

                    # Clear input field
                    pve.delete(0, tk.END)
                except Exception as e:
                    print(f"Error deleting data: {e}")

        delete_button = tk.Button(framevad, text="Delete Place", command=save_data, bg="#001f3d", fg="#ffd700", font=("Arial", 12))
        delete_button.grid(row=2, column=0, padx=10, pady=10)
        back_button = tk.Button(framevad, text="Back", command=lambda: placea(place), bg="#001f3d", fg="#ffd700", font=("Arial", 12))
        back_button.grid(row=2, column=1, padx=10, pady=10)

    vi="Welcome"
    vs="Select Option"

    labeli = tk.Label(frameva, text=vi, bg="#001f3d", font=("Arial", 30, "bold"), fg="#ffd700")
    labels = tk.Label(frameva, text=vs, bg="#001f3d", font=("Arial", 22, "bold"), fg="#ffd700")
    vi = tk.Button(frameva, text="Insert",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15),command=insertv)
    vd = tk.Button(frameva, text="Delete",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15),command=delete)
    vu = tk.Button(frameva, text="Update",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15),command=update)
    vs = tk.Button(frameva, text="Search",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15),command=search)
    
    labeli.grid(row=0, column=0, padx=10, pady=10, sticky="news", rowspan=3, columnspan=5)
    labels.grid(row=3, column=0, padx=10, pady=10, sticky="news", columnspan=5)
    vi.grid(row=4, column=0, padx=10, pady=10, sticky="ew")  
    vd.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
    vu.grid(row=4, column=2, padx=10, pady=10, sticky="ew")
    vs.grid(row=4, column=3, padx=10, pady=10, sticky="ew")

    back_button = tk.Button(frameva, text="Back", command=admin_page,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    back_button.grid(row=5, column=0, padx=10, pady=10,columnspan=4, sticky="ew")
    
    frameva.grid_rowconfigure(0, weight=1) 
    frameva.grid_rowconfigure(1, weight=1) 
    frameva.grid_rowconfigure(3, weight=1) 
    frameva.grid_rowconfigure(4, weight=1) 
    frameva.grid_columnconfigure(0, weight=1)
    frameva.grid_columnconfigure(1, weight=1)
    frameva.grid_columnconfigure(2, weight=1)
    frameva.grid_columnconfigure(3, weight=1)

def valsad():
    clear_widgets()
    framev = tk.Frame(window, bg="#001f3d")
    framev.pack(expand=True)

    vi = """\tValsad
    Nestled along the Arabian Sea, Valsad is a picturesque district in the southern part of Gujarat, India. 
    Known for its stunning beaches, lush greenery, and rich cultural heritage, Valsad offers a delightful blend of 
    natural beauty and historical significance."""

    def show_how_to_reach():
        top = tk.Toplevel(window)
        top.title("How to reach?")
        top.geometry("400x300")
        top.configure(bg="#001f3d")

        message = """You can reach Valsad by:\n
        - Train: Valsad Railway Station\n
        - Bus: Valsad Bus Station\n
        - Air: Surat Airport (nearest airport)"""
        
        label = tk.Label(top, text=message,  bg="#001f3d", fg="#ffd700", font=("Arial", 12), wraplength=350)
        label.pack(pady=20, padx=20)

        close_button = tk.Button(top, text="Close", command=top.destroy,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
        close_button.pack(pady=10)

    def tourist_attractions():
        clear_widgets()
        frametv = tk.Frame(window, bg="#2C2C2C")
        frametv.pack(expand=True)

        title = tk.Label(frametv, text="Tourist Attractions in Valsad", bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 18, "bold"))
        title.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        def show_details(event):
            selected_place = listbox.get(listbox.curselection())
            details = vr[selected_place]
            detail_label.config(text=details)

        listbox = tk.Listbox(frametv, bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 14), selectbackground="#FFD700", selectforeground="#2C2C2C")
        for place in vr.keys():
            listbox.insert(tk.END, place)
        listbox.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        listbox.bind('<<ListboxSelect>>', show_details)

        detail_label = tk.Label(frametv, text="Select a place to see details", bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 14, "italic"), wraplength=800)
        detail_label.grid(row=2, column=0, padx=20, pady=20, sticky="n")

        back_button = tk.Button(frametv, text="Back", command=valsad, bg="#FFD700", fg="#2C2C2C", font=("Helvetica", 12, "bold"))
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        frametv.grid_rowconfigure(0, weight=1)
        frametv.grid_rowconfigure(1, weight=1)
        frametv.grid_rowconfigure(2, weight=1)
        frametv.grid_rowconfigure(3, weight=1)
        frametv.grid_columnconfigure(0, weight=1)

    def hotel():
        h = """Hotels to Stay in Valsad:\n
        - The Umbergaon Club\n
        - Hotel Grandeur & Vista Rooms\n
        - Hotel Orizon\n
        - Pravashigruh"""
        tkinter.messagebox.showinfo(title="Hotels To Stay", message=h)   

    labelvi = tk.Label(framev, text=vi,  bg="#001f3d", fg="#ffd700", font=("Arial", 12), wraplength=800)
    labelvi.grid(row=0, column=0, padx=10, pady=10, sticky="news", rowspan=3, columnspan=4)
    hb = tk.Button(framev, text="How to reach", command=show_how_to_reach,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    hb.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    tb = tk.Button(framev, text="Tourist Attractions", command=tourist_attractions,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    tb.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
    htb=tk.Button(framev, text="Hotels to stay", command=hotel,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    htb.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

    back_button = tk.Button(framev, text="Back to Introduction", command=introduction,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    back_button.grid(row=4, column=0,columnspan=3, padx=10, pady=10, sticky="ew")

    framev.grid_rowconfigure(0, weight=1)
    framev.grid_rowconfigure(1, weight=1)
    framev.grid_columnconfigure(0, weight=1)
    framev.grid_columnconfigure(1,weight=1)
    framev.grid_columnconfigure(2,weight=1)

def navsari():
    clear_widgets()
    framen = tk.Frame(window, bg="#001f3d")
    framen.pack(expand=True)

    ni = """\tNavsari
    Navsari, a historic city in Gujarat, India, offers a unique blend of ancient heritage and modern amenities. 
    With its rich cultural tapestry, diverse population, and historical landmarks, Navsari provides a fascinating glimpse into Gujarat's past. 
    Visitors can explore ancient temples, mosques, and colonial-era buildings, indulge in delicious local cuisine, and experience the serene atmosphere of this charming city."""

    def show_how_to_reachn():
        mn = """You can reach Navsari by:\n
    - Train: Navsari Railway Station\n
    - Bus: Navsari Bus Station\n
    - Air: Surat Airport (nearest airport)"""
        tkinter.messagebox.showinfo(title="How to reach?", message=mn)

    def tourist_attractionsn():
        clear_widgets()
        frametn = tk.Frame(window, bg="#2C2C2C")
        frametn.pack(expand=True)

        titlen = tk.Label(frametn, text="Tourist Attractions in Navsari", bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 18, "bold"))
        titlen.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        def show_detailsn(event):
            selected_place = listbox.get(listbox.curselection())
            details = nr[selected_place]
            detail_label.config(text=details)

        listbox = tk.Listbox(frametn, bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 14), selectbackground="#FFD700", selectforeground="#2C2C2C")
        for place in nr.keys():
            listbox.insert(tk.END, place)
        listbox.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        listbox.bind('<<ListboxSelect>>', show_detailsn)

        detail_label = tk.Label(frametn, text="Select a place to see details", bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 14, "italic"), wraplength=800)
        detail_label.grid(row=2, column=0, padx=20, pady=20, sticky="n")

        back_button = tk.Button(frametn, text="Back", command=navsari, bg="#FFD700", fg="#2C2C2C", font=("Helvetica", 12, "bold"))
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        frametn.grid_rowconfigure(0, weight=1)
        frametn.grid_rowconfigure(1, weight=1)
        frametn.grid_rowconfigure(2, weight=1)
        frametn.grid_rowconfigure(3, weight=1)
        frametn.grid_columnconfigure(0, weight=1)

    def hoteln():
        hn = """Hotels to Stay in Navsari:\n
        - Uday Palace\n
        - Hotel Royal Regency\n
        - GD Hotel\n
        - Lords Eco Inn Navsari"""
        tkinter.messagebox.showinfo(title="Hotels To Stay", message=hn)   

    labelni = tk.Label(framen, text=ni,  bg="#001f3d", fg="#ffd700", font=("Arial", 12), wraplength=800)
    labelni.grid(row=0, column=0, padx=10, pady=10, sticky="news", rowspan=3, columnspan=4)
    hbn = tk.Button(framen, text="How to reach", command=show_how_to_reachn,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    hbn.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    tbn= tk.Button(framen, text="Tourist Attractions", command=tourist_attractionsn,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    tbn.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
    htbn=tk.Button(framen, text="Hotels to stay", command=hoteln,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    htbn.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

    back_button = tk.Button(framen, text="Back to Introduction", command=introduction,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    back_button.grid(row=4, column=0, padx=10, pady=10,columnspan=3, sticky="ew")

    framen.grid_rowconfigure(0, weight=1)
    framen.grid_rowconfigure(1, weight=1)
    framen.grid_columnconfigure(0, weight=1)
    framen.grid_columnconfigure(1,weight=1)
    framen.grid_columnconfigure(2,weight=1)

def dang():
    clear_widgets()
    framed = tk.Frame(window, bg="#001f3d")
    framed.pack(expand=True)

    di = """\tDang
    Dang, a picturesque district nestled in the southeastern part of Gujarat, India, is a treasure trove of natural beauty and cultural richness. 
    Known for its lush green landscapes, dense forests, and tribal heritage, Dang offers a unique and unforgettable experience for visitors."""

    def show_how_to_reachd():
        md = """You can reach Dang by:\n
    - Train: Waghai Railway Station (nearest railway station)\n
    - Bus: Ahwa Bus Station\n
    - Air: Surat Airport (nearest airport)"""
        tkinter.messagebox.showinfo(title="How to reach?", message=md)

    def tourist_attractionsd():
        clear_widgets()
        frametd = tk.Frame(window, bg="#2C2C2C")
        frametd.pack(expand=True)

        titled = tk.Label(frametd, text="Tourist Attractions in Dang", bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 18, "bold"))
        titled.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        def show_detailsd(event):
            selected_place = listbox.get(listbox.curselection())
            details = dr[selected_place]
            detail_label.config(text=details)

        listbox = tk.Listbox(frametd, bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 14), selectbackground="#FFD700", selectforeground="#2C2C2C")
        for place in dr.keys():
            listbox.insert(tk.END, place)
        listbox.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        listbox.bind('<<ListboxSelect>>', show_detailsd)

        detail_label = tk.Label(frametd, text="Select a place to see details", bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 14, "italic"), wraplength=800)
        detail_label.grid(row=2, column=0, padx=20, pady=20, sticky="n")

        back_button = tk.Button(frametd, text="Back", command=dang, bg="#FFD700", fg="#2C2C2C", font=("Helvetica", 12, "bold"))
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        frametd.grid_rowconfigure(0, weight=1)
        frametd.grid_rowconfigure(1, weight=1)
        frametd.grid_rowconfigure(2, weight=1)
        frametd.grid_rowconfigure(3, weight=1)
        frametd.grid_columnconfigure(0, weight=1)

    def hoteld():
        hd = """Hotels to Stay in Dang:\n
        - Sunotel\n
        - Patang Residency\n
        - Savshanti Lake Resort\n
        - Hotel Ananda"""
        tkinter.messagebox.showinfo(title="Hotels To Stay", message=hd)   

    labeldi = tk.Label(framed, text=di,  bg="#001f3d", fg="#ffd700", font=("Arial", 12), wraplength=800)
    labeldi.grid(row=0, column=0, padx=10, pady=10, sticky="news", rowspan=3, columnspan=4)
    hbd = tk.Button(framed, text="How to reach", command=show_how_to_reachd,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    hbd.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    tbd= tk.Button(framed, text="Tourist Attractions", command=tourist_attractionsd,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    tbd.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
    htbd=tk.Button(framed, text="Hotels to stay", command=hoteld,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    htbd.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

    back_button = tk.Button(framed, text="Back to Introduction", command=introduction,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    back_button.grid(row=4, column=0, padx=10, pady=10,columnspan=3, sticky="ew")

    framed.grid_rowconfigure(0, weight=1)
    framed.grid_rowconfigure(1, weight=1)
    framed.grid_columnconfigure(0, weight=1)
    framed.grid_columnconfigure(1,weight=1)
    framed.grid_columnconfigure(2,weight=1)

def surat():
    clear_widgets()
    frames = tk.Frame(window, bg="#001f3d")
    frames.pack(expand=True)

    si = """\tSurat
    Surat is a bustling city in Gujarat, India, renowned for its textile industry and diamond trade. 
    It offers a blend of modern amenities and cultural heritage, with historical sites, diverse religious landmarks, and delicious street food."""

    def show_how_to_reachs():
        ms = """You can reach Surat by:
    - Train: Surat Railway Station, a major hub with connections to major cities.
    - Bus: Surat Central Bus Station, providing access to nearby regions and states.
    - Air: Surat International Airport, with flights connecting to major cities in India and select international destinations."""

        tkinter.messagebox.showinfo(title="How to reach?", message=ms)

    def tourist_attractionss():
        clear_widgets()
        framets = tk.Frame(window, bg="#2C2C2C")
        framets.pack(expand=True)

        titles = tk.Label(framets, text="Tourist Attractions in Surat", bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 18, "bold"))
        titles.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        def show_detailss(event):
            selected_place = listbox.get(listbox.curselection())
            details = sr[selected_place]
            detail_label.config(text=details)

        listbox = tk.Listbox(framets, bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 14), selectbackground="#FFD700", selectforeground="#2C2C2C")
        for place in sr.keys():
            listbox.insert(tk.END, place)
        listbox.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        listbox.bind('<<ListboxSelect>>', show_detailss)

        detail_label = tk.Label(framets, text="Select a place to see details", bg="#2C2C2C", fg="#FFD700", font=("Helvetica", 14, "italic"), wraplength=800)
        detail_label.grid(row=2, column=0, padx=20, pady=20, sticky="n")

        back_button = tk.Button(framets, text="Back", command=surat, bg="#FFD700", fg="#2C2C2C", font=("Helvetica", 12, "bold"))
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        framets.grid_rowconfigure(0, weight=1)
        framets.grid_rowconfigure(1, weight=1)
        framets.grid_rowconfigure(2, weight=1)
        framets.grid_rowconfigure(3, weight=1)
        framets.grid_columnconfigure(0, weight=1)

    def hotels():
        hs = """Hotels to Stay in Surat:\n
        - Courtyard Surat\n
        - The World\n
        - Lords Plaza - Surat\n
        - Park Inn by Radisson Surat"""
        tkinter.messagebox.showinfo(title="Hotels To Stay", message=hs)   

    labelsi = tk.Label(frames, text=si,  bg="#001f3d", fg="#ffd700", font=("Arial", 12), wraplength=800)
    labelsi.grid(row=0, column=0, padx=10, pady=10, sticky="news", rowspan=3, columnspan=4)
    hbs = tk.Button(frames, text="How to reach", command=show_how_to_reachs,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    hbs.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    tbs= tk.Button(frames, text="Tourist Attractions", command=tourist_attractionss,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    tbs.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
    htbs=tk.Button(frames, text="Hotels to stay", command=hotels,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    htbs.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

    back_button = tk.Button(frames, text="Back to Introduction", command=introduction,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    back_button.grid(row=4, column=0, padx=10, pady=10,columnspan=3, sticky="ew")

    frames.grid_rowconfigure(0, weight=1)
    frames.grid_rowconfigure(1, weight=1)
    frames.grid_columnconfigure(0, weight=1)
    frames.grid_columnconfigure(1,weight=1)
    frames.grid_columnconfigure(2,weight=1)

def hi():
    clear_widgets()
    header_frame = tk.Frame(window, bg="#001f3d")
    header_frame.pack(fill="x", pady=20)

    load()

    label1 = tk.Label(header_frame, text="Hidden Gems Of Gujarat",bg="#001f3d", fg="#ffd700", font=("Arial", 30))
    label2 = tk.Label(header_frame, text="Welcome", bg="#001f3d", fg="#ffd700", font=("Arial", 20))
    label1.pack()
    label2.pack()

    button_frame = tk.Frame(window, bg="#001f3d")
    button_frame.pack(pady=20)

    continue_b = tk.Button(button_frame, text="Enter", command=introduction,bg="#001f3d", fg="#ffd700", font=("Arial", 15))
    continue_b.pack(side="left", padx=10)

    admin_b = tk.Button(button_frame, text="Admin", command=admin,bg="#001f3d", fg="#ffd700", font=("Arial", 15))
    admin_b.pack(side="left", padx=10)

def introduction():
    clear_widgets()
    framei = tk.Frame(window, bg="#001f3d")
    framei.pack(expand=True)

    # Introduction text
    i = """\tHidden Gems Of Gujarat
    Gujarat, a state in western India, is renowned for its vibrant culture, historical sites, and stunning landscapes.
    Many Gems are hidden in the southern part of Gujarat that consists of Valsad, Surat, Dang and Navsari.South Gujarat is a culturally rich and geographically diverse region. 
    Known for its lush landscapes, vibrant history, and significant economic contribution, this area comprises key districts like Valsad, Dang, Navsari, and Surat. 
    Each district has its unique appeal, from the urbanization and industrial prowess of Surat to the natural beauty and tribal heritage of the Dang district.
     """

    s = "Select The  You Want To Explore"
    
    labeli = tk.Label(framei, text=i, bg="#001f3d", font=("Arial", 13), fg="#ffd700")
    labels = tk.Label(framei, text=s, bg="#001f3d", font=("Arial", 12, "bold"), fg="#ffd700")
    vb = tk.Button(framei, text="Valsad",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15),command=valsad)
    db = tk.Button(framei, text="Dang",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15),command=dang)
    nb = tk.Button(framei, text="Navsari",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15),command=navsari)
    sb = tk.Button(framei, text="Surat",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15),command=surat)

    labeli.grid(row=0, column=0, padx=10, pady=10, sticky="news", rowspan=3, columnspan=4)
    labels.grid(row=3, column=0, padx=10, pady=10, sticky="news", columnspan=4)
    vb.grid(row=4, column=0, padx=10, pady=10, sticky="ew")  # Ensure buttons expand to fill space
    db.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
    nb.grid(row=4, column=2, padx=10, pady=10, sticky="ew")
    sb.grid(row=4, column=3, padx=10, pady=10, sticky="ew")

    back_button = tk.Button(framei, text="Back", command=hi,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
    back_button.grid(row=5, column=0,columnspan=4, padx=10, pady=10, sticky="ew")

    # Configure rows and columns to expand nicely
    framei.grid_rowconfigure(0, weight=1)  
    framei.grid_rowconfigure(1, weight=1)  
    framei.grid_rowconfigure(3, weight=1) 
    framei.grid_rowconfigure(4, weight=1) 
    framei.grid_columnconfigure(0, weight=1)
    framei.grid_columnconfigure(1, weight=1)
    framei.grid_columnconfigure(2, weight=1)
    framei.grid_columnconfigure(3, weight=1)


def admin_page():
        clear_widgets()
        frameap = tk.Frame(window, bg="#001f3d")
        frameap.pack(expand=True)

        s = "Select The Place You Want To Explore"
        labels = tk.Label(frameap, text=s, bg="#001f3d", font=("Arial", 12, "bold"), fg="#ffd700")

        vb = tk.Button(frameap, text="Valsad",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15), command=lambda: placea("Valsad"))
        db = tk.Button(frameap, text="Dang",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15), command=lambda: placea("Dang"))
        nb = tk.Button(frameap, text="Navsari",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15), command=lambda: placea("Navsari"))
        sb = tk.Button(frameap, text="Surat",  bg="#001f3d", fg="#ffd700", activebackground="red", font=("Arial", 15), command=lambda: placea("Surat"))

        labels.grid(row=3, column=0, padx=10, pady=10, sticky="news", columnspan=4)
        vb.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        db.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
        nb.grid(row=4, column=2, padx=10, pady=10, sticky="ew")
        sb.grid(row=4, column=3, padx=10, pady=10, sticky="ew")

        back_button = tk.Button(frameap, text="Back", command=admin,  bg="#001f3d", fg="#ffd700", font=("Arial", 12))
        back_button.grid(row=5, column=0, padx=10, pady=10,columnspan=4, sticky="ew")

        frameap.grid_rowconfigure(0, weight=1)
        frameap.grid_rowconfigure(1, weight=1)
        frameap.grid_rowconfigure(3, weight=1)
        frameap.grid_rowconfigure(4, weight=1)
        frameap.grid_columnconfigure(0, weight=1)
        frameap.grid_columnconfigure(1, weight=1)
        frameap.grid_columnconfigure(2, weight=1)
        frameap.grid_columnconfigure(3, weight=1)

def check():
    if admin_password.get() == "123":
        admin_page()
    else:
        tkinter.messagebox.showerror("Error", "Admin password is incorrect.")

def admin():
    clear_widgets()

    framea = tk.Frame(window, bg="#001f3d")
    framea.pack(expand=True)

    # Admin password input
    global admin_password
    admin_password = tk.StringVar()

    pl = tk.Label(framea, text="Enter Admin Password", bg="#001f3d", font=("Arial", 12, "bold"), fg="#ffd700")
    pw = tk.Entry(framea, show="*", textvariable=admin_password, font=("Arial", 12), width=20)
    pc = tk.Button(framea, text="Confirm",  bg="#001f3d", fg="#ffd700", font=("Arial", 15), command=check,height=1,width=6)
    back_button = tk.Button(framea, text="Back", command=hi,  bg="#001f3d", fg="#ffd700", font=("Arial", 15),height=1,width=6)

    pl.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    pw.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20))
    pc.grid(row=2, column=0)
    back_button.grid(row=2, column=1)
    
hi()

window.mainloop()
