//Maya ASCII 2018 scene
//Name: test_prMotionPath.ma
//Last modified: Thu, Oct 03, 2019 01:34:17 AM
//Codeset: 1252
requires maya "2018";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "CE5E5960-4F8C-78CD-4C47-14BACE3AF1F4";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -2.5639141423352512 4.473729643511918 10.883706039073111 ;
	setAttr ".r" -type "double3" -16.538352729604934 -14.20000000000022 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "81138384-4173-4638-2A58-5CAC4AE12E2B";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 13.134030398880936;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "D1CA3F84-42C0-B32E-7692-77A6836689CF";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "F8779FBD-4237-725E-6430-C4973D4DDCFD";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "8DD5A033-446D-EB76-6493-DEA4D10D1BED";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "B2C12D63-4595-AEF0-F34D-3DB68D091ED1";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "0AA982D4-4D23-654D-BB4F-E381D5AF841F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "58929AD0-4DE9-6325-5065-10B31A22EECE";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "curve1";
	rename -uid "C0041678-42D6-6299-94AB-E7AEEFAB63E8";
createNode nurbsCurve -n "curveShape1" -p "curve1";
	rename -uid "B3250865-4D80-32BE-216A-B69C2D53456E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 2 0 no 3
		7 0 0 0 1 2 2 2
		5
		-2 0.83760578522618712 1
		0 1.7148759246513274 -1
		2 0.76400401522016703 1
		4 0 -1
		6 1.198673128313589 1
		;
createNode transform -n "motionpath_cubes";
	rename -uid "2619EB22-44F3-82D4-6FA7-70B6E9DE9206";
createNode transform -n "motionpath_output_0" -p "motionpath_cubes";
	rename -uid "7C3FAA01-484E-A9E4-D864-C7869E322B02";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".smd" 7;
createNode mesh -n "motionpath_output_0Shape" -p "motionpath_output_0";
	rename -uid "0AA7410D-49A6-51D4-0897-32A224DF761C";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.33234507 0.33234507 -0.33234507 
		-0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 -0.33234507 
		-0.33234507 -0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 
		0.33234507 0.33234507 0.33234507 0.33234507 -0.33234507 0.33234507 0.33234507;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "motionpath_output_1" -p "motionpath_cubes";
	rename -uid "37E2A611-4FA6-3DE4-76B3-1D910BA46E78";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".smd" 7;
createNode mesh -n "motionpath_output_1Shape" -p "motionpath_output_1";
	rename -uid "07294252-498D-204B-055F-5D8587AB557D";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.33234507 0.33234507 -0.33234507 
		-0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 -0.33234507 
		-0.33234507 -0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 
		0.33234507 0.33234507 0.33234507 0.33234507 -0.33234507 0.33234507 0.33234507;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "motionpath_output_2" -p "motionpath_cubes";
	rename -uid "E3E13F88-4AF9-B5FF-220A-25A1780BE9D6";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".smd" 7;
createNode mesh -n "motionpath_output_2Shape" -p "motionpath_output_2";
	rename -uid "5BC97C6B-497A-3E70-01A4-98AB49BCAE9C";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.33234507 0.33234507 -0.33234507 
		-0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 -0.33234507 
		-0.33234507 -0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 
		0.33234507 0.33234507 0.33234507 0.33234507 -0.33234507 0.33234507 0.33234507;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "motionpath_output_3" -p "motionpath_cubes";
	rename -uid "15676098-400A-D744-1721-168E245E84A4";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".smd" 7;
createNode mesh -n "motionpath_output_3Shape" -p "motionpath_output_3";
	rename -uid "C91664BF-44D7-ED0D-7FB4-7A9AFB5A0021";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.33234507 0.33234507 -0.33234507 
		-0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 -0.33234507 
		-0.33234507 -0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 
		0.33234507 0.33234507 0.33234507 0.33234507 -0.33234507 0.33234507 0.33234507;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "motionpath_output_4" -p "motionpath_cubes";
	rename -uid "B1493523-4F2E-BC3D-5837-C6BB885CBCA3";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".smd" 7;
createNode mesh -n "motionpath_output_4Shape" -p "motionpath_output_4";
	rename -uid "0674BB06-4A1E-C40F-9183-29B9AA8E1CE6";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.33234507 0.33234507 -0.33234507 
		-0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 -0.33234507 
		-0.33234507 -0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 
		0.33234507 0.33234507 0.33234507 0.33234507 -0.33234507 0.33234507 0.33234507;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "motionpath_output_5" -p "motionpath_cubes";
	rename -uid "6098315A-42DA-2F65-6010-80AC21A4EC2B";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".smd" 7;
createNode mesh -n "motionpath_output_5Shape" -p "motionpath_output_5";
	rename -uid "6B70CA12-489F-0C49-4A07-0BA9254418F4";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.33234507 0.33234507 -0.33234507 
		-0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 -0.33234507 
		-0.33234507 -0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 
		0.33234507 0.33234507 0.33234507 0.33234507 -0.33234507 0.33234507 0.33234507;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "motionpath_output_6" -p "motionpath_cubes";
	rename -uid "69D5B9B7-4E4F-E2D2-5047-1ABE871966FE";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".smd" 7;
createNode mesh -n "motionpath_output_6Shape" -p "motionpath_output_6";
	rename -uid "D316EF77-4FDC-6326-9331-3480CA5A0E2C";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.33234507 0.33234507 -0.33234507 
		-0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 -0.33234507 
		-0.33234507 -0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 
		0.33234507 0.33234507 0.33234507 0.33234507 -0.33234507 0.33234507 0.33234507;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "motionpath_output_7" -p "motionpath_cubes";
	rename -uid "B27DE030-4D7F-49E6-24BC-6D86FF70CF36";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".smd" 7;
createNode mesh -n "motionpath_output_7Shape" -p "motionpath_output_7";
	rename -uid "C913F16B-48DD-4125-55A5-8AA0F7A13382";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.33234507 0.33234507 -0.33234507 
		-0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 -0.33234507 
		-0.33234507 -0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 
		0.33234507 0.33234507 0.33234507 0.33234507 -0.33234507 0.33234507 0.33234507;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "motionpath_output_8" -p "motionpath_cubes";
	rename -uid "7F832F2C-49F9-941D-13C1-E78358355095";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".smd" 7;
createNode mesh -n "motionpath_output_8Shape" -p "motionpath_output_8";
	rename -uid "ED48B0AB-4166-654A-8031-ADB320E3E46B";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.33234507 0.33234507 -0.33234507 
		-0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 -0.33234507 
		-0.33234507 -0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 
		0.33234507 0.33234507 0.33234507 0.33234507 -0.33234507 0.33234507 0.33234507;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "motionpath_output_9" -p "motionpath_cubes";
	rename -uid "5F86D7C3-44B1-D73D-C125-CD9D880AF0D0";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".smd" 7;
createNode mesh -n "motionpath_output_9Shape" -p "motionpath_output_9";
	rename -uid "FA9A2304-4BEE-60EC-F5EB-6C8AC39F9E6E";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.33234507 0.33234507 -0.33234507 
		-0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 -0.33234507 
		-0.33234507 -0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 
		0.33234507 0.33234507 0.33234507 0.33234507 -0.33234507 0.33234507 0.33234507;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "motionpath_output_10" -p "motionpath_cubes";
	rename -uid "5D3C8347-4358-CA37-6DD3-ED865DFCC8A2";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".smd" 7;
createNode mesh -n "motionpath_output_10Shape" -p "motionpath_output_10";
	rename -uid "B8BF1ADC-40B4-55EC-B936-97B1922777E5";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.33234507 0.33234507 -0.33234507 
		-0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 -0.33234507 
		-0.33234507 -0.33234507 0.33234507 -0.33234507 0.33234507 -0.33234507 -0.33234507 
		0.33234507 0.33234507 0.33234507 0.33234507 -0.33234507 0.33234507 0.33234507;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "prnode_cubes";
	rename -uid "5F638A5D-49D8-4437-8AF8-3EBEC5023B0F";
createNode transform -n "prnode_output_0" -p "prnode_cubes";
	rename -uid "D38C1108-4DA1-6EF1-74D1-5E9F8D06F641";
createNode mesh -n "prnode_output_0Shape" -p "prnode_output_0";
	rename -uid "F441B88E-4CCC-13F7-9262-E183B775F623";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.34747377 0.34747377 -0.34747377 
		-0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 -0.34747377 
		-0.34747377 -0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 
		0.34747377 0.34747377 0.34747377 0.34747377 -0.34747377 0.34747377 0.34747377;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "prnode_output_1" -p "prnode_cubes";
	rename -uid "1BCF0C7D-4749-3BFE-6D25-40BC793782CD";
createNode mesh -n "prnode_output_1Shape" -p "prnode_output_1";
	rename -uid "2DD1D540-4C1B-A3FF-4ED6-9E844D94D7C4";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.34747377 0.34747377 -0.34747377 
		-0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 -0.34747377 
		-0.34747377 -0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 
		0.34747377 0.34747377 0.34747377 0.34747377 -0.34747377 0.34747377 0.34747377;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "prnode_output_2" -p "prnode_cubes";
	rename -uid "2ADB4D87-4F70-738F-EAE7-3FB8B91B53F6";
createNode mesh -n "prnode_output_2Shape" -p "prnode_output_2";
	rename -uid "DF3F4301-425E-FFAC-9716-609CE275ADC0";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.34747377 0.34747377 -0.34747377 
		-0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 -0.34747377 
		-0.34747377 -0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 
		0.34747377 0.34747377 0.34747377 0.34747377 -0.34747377 0.34747377 0.34747377;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "prnode_output_3" -p "prnode_cubes";
	rename -uid "998EB418-4FDB-1224-0579-4BBB5B274018";
createNode mesh -n "prnode_output_3Shape" -p "prnode_output_3";
	rename -uid "9CAA6420-474A-317E-AEE0-BEBE178C21D7";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.34747377 0.34747377 -0.34747377 
		-0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 -0.34747377 
		-0.34747377 -0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 
		0.34747377 0.34747377 0.34747377 0.34747377 -0.34747377 0.34747377 0.34747377;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "prnode_output_4" -p "prnode_cubes";
	rename -uid "5173B639-4771-20E5-717F-99BC61763B91";
createNode mesh -n "prnode_output_4Shape" -p "prnode_output_4";
	rename -uid "31E8154D-4CEF-8BD9-2588-95A059A749F6";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.34747377 0.34747377 -0.34747377 
		-0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 -0.34747377 
		-0.34747377 -0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 
		0.34747377 0.34747377 0.34747377 0.34747377 -0.34747377 0.34747377 0.34747377;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "prnode_output_5" -p "prnode_cubes";
	rename -uid "726A0F8B-4C3B-25C0-A981-17977A623B2A";
createNode mesh -n "prnode_output_5Shape" -p "prnode_output_5";
	rename -uid "7CFA868F-4578-D850-8342-F797E2539C04";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.34747377 0.34747377 -0.34747377 
		-0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 -0.34747377 
		-0.34747377 -0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 
		0.34747377 0.34747377 0.34747377 0.34747377 -0.34747377 0.34747377 0.34747377;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "prnode_output_6" -p "prnode_cubes";
	rename -uid "C5BCC125-4483-7751-28C7-E8894BD4E3B8";
createNode mesh -n "prnode_output_6Shape" -p "prnode_output_6";
	rename -uid "63D21C7C-4717-3B42-9F65-CCA34F6DF447";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.34747377 0.34747377 -0.34747377 
		-0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 -0.34747377 
		-0.34747377 -0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 
		0.34747377 0.34747377 0.34747377 0.34747377 -0.34747377 0.34747377 0.34747377;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "prnode_output_7" -p "prnode_cubes";
	rename -uid "6992363F-4D04-EEF8-914F-1EBB2B84225B";
createNode mesh -n "prnode_output_7Shape" -p "prnode_output_7";
	rename -uid "848A8E8A-46C3-3709-F1F2-C99FEA8C3E4B";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.34747377 0.34747377 -0.34747377 
		-0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 -0.34747377 
		-0.34747377 -0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 
		0.34747377 0.34747377 0.34747377 0.34747377 -0.34747377 0.34747377 0.34747377;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "prnode_output_8" -p "prnode_cubes";
	rename -uid "774B2319-40BC-E94F-80AF-CD914759BC1B";
createNode mesh -n "prnode_output_8Shape" -p "prnode_output_8";
	rename -uid "BFFC69E8-466C-72A4-F4B7-A59CA92D4373";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.34747377 0.34747377 -0.34747377 
		-0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 -0.34747377 
		-0.34747377 -0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 
		0.34747377 0.34747377 0.34747377 0.34747377 -0.34747377 0.34747377 0.34747377;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "prnode_output_9" -p "prnode_cubes";
	rename -uid "9933962C-4B9B-F473-2DBA-3EB06ED84BDE";
createNode mesh -n "prnode_output_9Shape" -p "prnode_output_9";
	rename -uid "B716BED6-4EC0-48DC-63D2-E1BE377F016F";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.34747377 0.34747377 -0.34747377 
		-0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 -0.34747377 
		-0.34747377 -0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 
		0.34747377 0.34747377 0.34747377 0.34747377 -0.34747377 0.34747377 0.34747377;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "prnode_output_10" -p "prnode_cubes";
	rename -uid "7EFA3264-4166-7F7B-A73F-73B744594529";
createNode mesh -n "prnode_output_10Shape" -p "prnode_output_10";
	rename -uid "3DD41F35-491D-03BA-8341-96A832923EFC";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.34747377 0.34747377 -0.34747377 
		-0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 -0.34747377 
		-0.34747377 -0.34747377 0.34747377 -0.34747377 0.34747377 -0.34747377 -0.34747377 
		0.34747377 0.34747377 0.34747377 0.34747377 -0.34747377 0.34747377 0.34747377;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "uValue_locator";
	rename -uid "BEC34A7C-4820-CB39-FA16-FBA71C5AA4E6";
	addAttr -ci true -k true -sn "uValue0" -ln "uValue0" -at "double";
	addAttr -ci true -k true -sn "uValue1" -ln "uValue1" -dv 0.1 -at "double";
	addAttr -ci true -k true -sn "uValue2" -ln "uValue2" -dv 0.2 -at "double";
	addAttr -ci true -k true -sn "uValue3" -ln "uValue3" -dv 0.30000000000000004 -at "double";
	addAttr -ci true -k true -sn "uValue4" -ln "uValue4" -dv 0.4 -at "double";
	addAttr -ci true -k true -sn "uValue5" -ln "uValue5" -dv 0.5 -at "double";
	addAttr -ci true -k true -sn "uValue6" -ln "uValue6" -dv 0.60000000000000009 -at "double";
	addAttr -ci true -k true -sn "uValue7" -ln "uValue7" -dv 0.70000000000000007 -at "double";
	addAttr -ci true -k true -sn "uValue8" -ln "uValue8" -dv 0.8 -at "double";
	addAttr -ci true -k true -sn "uValue9" -ln "uValue9" -dv 0.9 -at "double";
	addAttr -ci true -k true -sn "uValue10" -ln "uValue10" -dv 1 -at "double";
	addAttr -ci true -sn "fractionMode" -ln "fractionMode" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".uValue0";
	setAttr -k on ".uValue1";
	setAttr -k on ".uValue2";
	setAttr -k on ".uValue3";
	setAttr -k on ".uValue4";
	setAttr -k on ".uValue5";
	setAttr -k on ".uValue6";
	setAttr -k on ".uValue7";
	setAttr -k on ".uValue8";
	setAttr -k on ".uValue9";
	setAttr -k on ".uValue10";
	setAttr -k on ".fractionMode" yes;
createNode locator -n "uValue_locatorShape" -p "uValue_locator";
	rename -uid "84699D8C-471A-1CE2-A032-BB93D63E747A";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.6 0.6 0.6 ;
createNode transform -n "annotation1" -p "uValue_locator";
	rename -uid "FFA6F9C0-41E0-01F5-20BD-E997EF979DAD";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
createNode annotationShape -n "annotationShape1" -p "annotation1";
	rename -uid "43458E85-41E9-548B-9B1E-119C1575BBED";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" " uValue";
	setAttr ".daro" no;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "22336D3E-4B18-E192-651A-4192818D2714";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "1AC08EE2-401A-6250-F08A-3E9818AD0FA9";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "2766708C-4075-971E-7ED7-8AA20727A6DA";
createNode displayLayerManager -n "layerManager";
	rename -uid "2F4F0DA5-4E5F-2A02-2F73-90B556FC3CB1";
createNode displayLayer -n "defaultLayer";
	rename -uid "88A67CB6-4713-8DFD-6E23-3CA78197C0FB";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "0435C8BF-445D-E227-3613-E78670B5127E";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "B4796BC8-4092-6F2B-13A9-E88CC2A3DB92";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "AEFA8DE3-4407-3170-F2C2-40A1C5471C89";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode motionPath -n "motionPath_0";
	rename -uid "DEC9C9D7-4448-5E36-1B9A-658C4BA08F9D";
	setAttr ".fm" yes;
createNode motionPath -n "motionPath_1";
	rename -uid "738E2AB2-427A-3EA6-178A-FC917E846D41";
	setAttr ".fm" yes;
createNode motionPath -n "motionPath_2";
	rename -uid "04422E6A-4847-9613-3771-C99D43FDCEFF";
	setAttr ".fm" yes;
createNode motionPath -n "motionPath_3";
	rename -uid "24245B7C-4BAA-93DB-B2E1-A59A4C20C73C";
	setAttr ".fm" yes;
createNode motionPath -n "motionPath_4";
	rename -uid "67252F26-4FF1-8F39-E3CD-A99D9542227D";
	setAttr ".fm" yes;
createNode motionPath -n "motionPath_5";
	rename -uid "6833233F-4886-16A5-C859-7BB5C94F3019";
	setAttr ".fm" yes;
createNode motionPath -n "motionPath_6";
	rename -uid "C1C9ACE0-4A84-E297-2936-448A17C8B492";
	setAttr ".fm" yes;
createNode motionPath -n "motionPath_7";
	rename -uid "64CE8C43-4AEB-561B-8860-629B95E9EDDE";
	setAttr ".fm" yes;
createNode motionPath -n "motionPath_8";
	rename -uid "7417EB05-41EC-02CB-B6CD-85AA6567DA0B";
	setAttr ".fm" yes;
createNode motionPath -n "motionPath_9";
	rename -uid "A90FDBB5-4817-24CC-6394-2494055973EC";
	setAttr ".fm" yes;
createNode motionPath -n "motionPath_10";
	rename -uid "D497B2D8-4A12-CD2B-FA32-A88D86CEF27D";
	setAttr ".fm" yes;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "F494C83A-4C9B-9E73-BFBC-EE84AF68A5D7";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -649.84522924290911 -392.29219889877521 ;
	setAttr ".tgi[0].vh" -type "double2" 452.11355393569659 443.49796841808075 ;
	setAttr -s 3 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -535.1434326171875;
	setAttr ".tgi[0].ni[0].y" 208.3079833984375;
	setAttr ".tgi[0].ni[0].nvs" 18305;
	setAttr ".tgi[0].ni[1].x" 131.42857360839844;
	setAttr ".tgi[0].ni[1].y" 118.57142639160156;
	setAttr ".tgi[0].ni[1].nvs" 18449;
	setAttr ".tgi[0].ni[2].x" -512.45318603515625;
	setAttr ".tgi[0].ni[2].y" -7.4765663146972656;
	setAttr ".tgi[0].ni[2].nvs" 1923;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -s 22 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "motionPath_0.ac" "motionpath_output_0.t";
connectAttr "motionPath_1.ac" "motionpath_output_1.t";
connectAttr "motionPath_2.ac" "motionpath_output_2.t";
connectAttr "motionPath_3.ac" "motionpath_output_3.t";
connectAttr "motionPath_4.ac" "motionpath_output_4.t";
connectAttr "motionPath_5.ac" "motionpath_output_5.t";
connectAttr "motionPath_6.ac" "motionpath_output_6.t";
connectAttr "motionPath_7.ac" "motionpath_output_7.t";
connectAttr "motionPath_8.ac" "motionpath_output_8.t";
connectAttr "motionPath_9.ac" "motionpath_output_9.t";
connectAttr "motionPath_10.ac" "motionpath_output_10.t";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "curveShape1.ws" "motionPath_0.gp";
connectAttr "uValue_locator.uValue0" "motionPath_0.u";
connectAttr "curveShape1.ws" "motionPath_1.gp";
connectAttr "uValue_locator.uValue1" "motionPath_1.u";
connectAttr "curveShape1.ws" "motionPath_2.gp";
connectAttr "uValue_locator.uValue2" "motionPath_2.u";
connectAttr "curveShape1.ws" "motionPath_3.gp";
connectAttr "uValue_locator.uValue3" "motionPath_3.u";
connectAttr "curveShape1.ws" "motionPath_4.gp";
connectAttr "uValue_locator.uValue4" "motionPath_4.u";
connectAttr "curveShape1.ws" "motionPath_5.gp";
connectAttr "uValue_locator.uValue5" "motionPath_5.u";
connectAttr "curveShape1.ws" "motionPath_6.gp";
connectAttr "uValue_locator.uValue6" "motionPath_6.u";
connectAttr "curveShape1.ws" "motionPath_7.gp";
connectAttr "uValue_locator.uValue7" "motionPath_7.u";
connectAttr "curveShape1.ws" "motionPath_8.gp";
connectAttr "uValue_locator.uValue8" "motionPath_8.u";
connectAttr "curveShape1.ws" "motionPath_9.gp";
connectAttr "uValue_locator.uValue9" "motionPath_9.u";
connectAttr "curveShape1.ws" "motionPath_10.gp";
connectAttr "uValue_locator.uValue10" "motionPath_10.u";
connectAttr "curveShape1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "motionpath_output_0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "uValue_locator.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "motionpath_output_0Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "prnode_output_0Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "motionpath_output_1Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "prnode_output_1Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "motionpath_output_2Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "prnode_output_2Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "motionpath_output_3Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "prnode_output_3Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "motionpath_output_4Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "prnode_output_4Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "motionpath_output_5Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "prnode_output_5Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "motionpath_output_6Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "prnode_output_6Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "motionpath_output_7Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "prnode_output_7Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "motionpath_output_8Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "prnode_output_8Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "motionpath_output_9Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "prnode_output_9Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "motionpath_output_10Shape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "prnode_output_10Shape.iog" ":initialShadingGroup.dsm" -na;
// End of test_prMotionPath.ma
