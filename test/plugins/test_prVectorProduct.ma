//Maya ASCII 2018 scene
//Name: test_prVectorProduct.ma
//Last modified: Thu, Sep 19, 2019 01:46:10 AM
//Codeset: 1252
requires maya "2018";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "0C68873B-42E1-044A-9AC2-03AD22B3D66B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1.9943683937012813 2.2472090566148215 3.6676492436527539 ;
	setAttr ".r" -type "double3" -25.538352729610271 26.600000000001423 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "BCA98976-415B-B4E0-3363-7A8DC13AFFC9";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 5.8301329795065122;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "185734B7-4E71-54BE-0AED-54B33B57AF09";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "78AF314D-470D-FE68-C763-F4AD6F9CF944";
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
	rename -uid "9E54F35A-43C4-CA46-C2DD-788533F9E9AD";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "DC9BA180-40FE-E3E3-7412-44B2D01BBD40";
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
	rename -uid "861D92A0-48DE-0615-E46A-3C859E556EE6";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "77D5F330-4ED6-96C2-23CE-46A99D981A83";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "input1";
	rename -uid "28FBE789-448C-F476-A559-76871E79292C";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 1 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "input1Shape" -p "input1";
	rename -uid "7D8C19ED-4705-89CF-2028-37B507272DA7";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "input1_annotation" -p "input1";
	rename -uid "9CA2444A-4CBF-61BF-D0AC-86B41CBC42FE";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
createNode annotationShape -n "input1_annotationShape" -p "input1_annotation";
	rename -uid "BC5451FB-4E6A-6906-78FB-89AF2B2593EF";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" "input1";
createNode transform -n "input2";
	rename -uid "140A038C-436B-BFC2-D635-AF840BFDB95D";
	addAttr -ci true -sn "scalar" -ln "scalar" -dv 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1 0 0 ;
	setAttr ".r" -type "double3" 0 0 -45 ;
	setAttr -k on ".scalar";
createNode locator -n "input2Shape" -p "input2";
	rename -uid "FB8522BD-443A-16C9-F627-4F94E4AE0308";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "input2_annotation" -p "input2";
	rename -uid "35F0F023-4F54-566D-85AA-4AA3A1B33C1D";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
createNode annotationShape -n "input2_annotationShape" -p "input2_annotation";
	rename -uid "AFF88E38-4914-412A-DC28-68A10C35C535";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" "input2_matrix_scalar";
createNode transform -n "global_transform";
	rename -uid "EF2FD44E-410E-38BF-968D-17850C9EC282";
	addAttr -ci true -sn "scalar" -ln "scalar" -dv 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -k on ".scalar";
createNode locator -n "global_transformShape" -p "global_transform";
	rename -uid "54F9A0EE-4BE2-0040-4B3F-ADA234A54D4D";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "globalMatrix_annotation" -p "global_transform";
	rename -uid "C37AB00E-4750-BE31-447F-5389FE6F7BB6";
	addAttr -ci true -sn "scalar" -ln "scalar" -dv 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr -k on ".scalar";
createNode annotationShape -n "globalMatrix_annotationShape" -p "globalMatrix_annotation";
	rename -uid "7B84363E-4519-F7C0-5D39-6E9AEF17BFB3";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" "globalScalar_globalMatrix";
	setAttr ".daro" no;
createNode transform -n "DONT_TOUCH";
	rename -uid "AA6874C5-4D10-BF96-AFBF-CA976CB3225B";
createNode transform -n "noOperation_result" -p "DONT_TOUCH";
	rename -uid "70567EA2-4B28-4DBE-2870-4DA1366A5F2C";
createNode transform -n "noOperation_vectorProduct_output" -p "noOperation_result";
	rename -uid "53EE2F68-45B1-F180-E3AB-AEAFFF1229E9";
createNode mesh -n "noOperation_vectorProduct_outputShape" -p "noOperation_vectorProduct_output";
	rename -uid "AE437293-4800-0F9B-57B8-1F875787A15D";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39099032 0.39099032 -0.39099032 
		-0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 -0.39099032 
		-0.39099032 -0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 
		0.39099032 0.39099032 0.39099032 0.39099032 -0.39099032 0.39099032 0.39099032;
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
createNode transform -n "noOperation_prVectorProduct_output_0" -p "noOperation_result";
	rename -uid "414A277B-4DD3-4F2A-1D11-6F82BA5F6B70";
createNode mesh -n "noOperation_prVectorProduct_output_0Shape" -p "noOperation_prVectorProduct_output_0";
	rename -uid "AA33CF02-45BC-EA3E-D820-AE886B5A601D";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39746848 0.39746848 -0.39746848 
		-0.39746848 0.39746848 -0.39746848 0.39746848 -0.49746844 -0.39746848 -0.39746848 
		-0.49746844 -0.39746848 0.39746848 -0.49746844 0.39746848 -0.39746848 -0.49746844 
		0.39746848 0.39746848 0.39746848 0.39746848 -0.39746848 0.39746848 0.39746848;
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
createNode transform -n "noOperation_prVectorProduct_output_2" -p "noOperation_result";
	rename -uid "450411A6-446B-940D-003C-B397F0D77ED7";
createNode mesh -n "noOperation_prVectorProduct_output_2Shape" -p "noOperation_prVectorProduct_output_2";
	rename -uid "963848E4-4C3B-3812-5443-EAA712E04978";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.60253149 0.60253149 -0.39746851 
		-0.39746854 0.60253137 -0.60253149 0.39746851 -0.39746857 -0.39746848 -0.60253143 
		-0.39746842 -0.60253143 0.39746848 -0.50253147 0.60253149 -0.60253149 -0.50253153 
		0.39746848 0.60253143 0.49746844 0.60253143 -0.39746854 0.49746856 0.39746857;
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
createNode transform -n "dotProduct_result" -p "DONT_TOUCH";
	rename -uid "4BC4D363-4197-39DA-C0C7-8FA9E28B7347";
createNode transform -n "dotProduct_vectorProduct_output" -p "dotProduct_result";
	rename -uid "8E04E653-49E5-84FC-79EC-1981794A81EB";
createNode mesh -n "dotProduct_vectorProduct_outputShape" -p "dotProduct_vectorProduct_output";
	rename -uid "BF1F0B1F-4568-F397-EB67-E1B9ABAE9E55";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39099032 0.39099032 -0.39099032 
		-0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 -0.39099032 
		-0.39099032 -0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 
		0.39099032 0.39099032 0.39099032 0.39099032 -0.39099032 0.39099032 0.39099032;
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
createNode transform -n "dotProduct_prVectorProduct_output_0" -p "dotProduct_result";
	rename -uid "147D6430-4108-2E4A-38C7-4786DD152C5F";
createNode mesh -n "dotProduct_prVectorProduct_output_0Shape" -p "dotProduct_prVectorProduct_output_0";
	rename -uid "6A2AA0A0-4943-92E9-EA16-6A96A9C4E8F9";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.375 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39746848 0.39746848 -0.39746848 
		-0.39746848 0.39746848 -0.39746848 0.39746848 -0.5 -0.39746848 -0.39746848 -0.5 -0.39746848 
		0.39746848 -0.5 0.39746848 -0.39746848 -0.5 0.39746848 0.39746848 0.39746848 0.39746848 
		-0.39746848 0.39746848 0.39746848;
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
createNode transform -n "dotProduct_prVectorProduct_output_2" -p "dotProduct_result";
	rename -uid "3C288495-4C31-ACFD-3B15-1DA7AD83C496";
createNode mesh -n "dotProduct_prVectorProduct_output_2Shape" -p "dotProduct_prVectorProduct_output_2";
	rename -uid "F7675FDB-482E-04C7-1679-71AA2BA574C8";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.375 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.60253149 0.60253149 -0.39746851 
		-0.39746854 0.60253137 -0.60253149 0.39746851 -0.39746857 -0.39746848 -0.60253143 
		-0.39746842 -0.60253143 0.39746848 -0.5 0.60253149 -0.60253149 -0.5 0.39746848 0.60253143 
		0.5 0.60253143 -0.39746854 0.5 0.39746857;
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
createNode transform -n "crossProduct_result" -p "DONT_TOUCH";
	rename -uid "3211DBAC-4BB9-74D5-352C-B880F33972DE";
createNode transform -n "crossProduct_vectorProduct_output" -p "crossProduct_result";
	rename -uid "CD959262-4E20-DC21-13AD-8D8A66524898";
createNode mesh -n "crossProduct_vectorProduct_outputShape" -p "crossProduct_vectorProduct_output";
	rename -uid "0D801201-4B61-366B-1816-5794A3E21694";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39099032 0.39099032 -0.39099032 
		-0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 -0.39099032 
		-0.39099032 -0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 
		0.39099032 0.39099032 0.39099032 0.39099032 -0.39099032 0.39099032 0.39099032;
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
createNode transform -n "crossProduct_prVectorProduct_output_0" -p "crossProduct_result";
	rename -uid "4317B2C4-4832-357B-19AE-4B837158C810";
createNode mesh -n "crossProduct_prVectorProduct_output_0Shape" -p "crossProduct_prVectorProduct_output_0";
	rename -uid "6BC11D85-481A-182E-34E1-FB810452DA8F";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39746848 0.39746848 -0.39746848 
		-0.39746848 0.39746848 -0.39746848 0.39746848 -0.5 -0.39746848 -0.39746848 -0.5 -0.39746848 
		0.39746848 -0.5 0.39746848 -0.39746848 -0.5 0.39746848 0.39746848 0.39746848 0.39746848 
		-0.39746848 0.39746848 0.39746848;
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
createNode transform -n "crossProduct_prVectorProduct_output_2" -p "crossProduct_result";
	rename -uid "48A33855-4CEF-8A20-3F41-E1B550B06F9D";
createNode mesh -n "crossProduct_prVectorProduct_output_2Shape" -p "crossProduct_prVectorProduct_output_2";
	rename -uid "4EC77B7B-417A-9843-4E23-BEB66B467FDD";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.60253149 0.60253149 -0.39746851 
		-0.39746854 0.60253137 -0.60253149 0.39746851 -0.39746857 -0.39746848 -0.60253143 
		-0.39746842 -0.60253143 0.39746848 -0.5 0.60253149 -0.60253149 -0.5 0.39746848 0.60253143 
		0.5 0.60253143 -0.39746854 0.5 0.39746857;
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
createNode transform -n "vectorMatrixProduct_result" -p "DONT_TOUCH";
	rename -uid "41DF505C-40AB-C4D3-C97E-2497D2B73826";
createNode transform -n "vectorMatrixProduct_vectorProduct_output" -p "vectorMatrixProduct_result";
	rename -uid "7F9C38EA-4D4B-ABBC-D72A-C7AFD49173D8";
createNode mesh -n "vectorMatrixProduct_vectorProduct_outputShape" -p "vectorMatrixProduct_vectorProduct_output";
	rename -uid "BA5D14E9-47A0-144D-58A1-3D80D6CE54C3";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39099032 0.39099032 -0.39099032 
		-0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 -0.39099032 
		-0.39099032 -0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 
		0.39099032 0.39099032 0.39099032 0.39099032 -0.39099032 0.39099032 0.39099032;
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
createNode transform -n "vectorMatrixProduct_prVectorProduct_output_0" -p "vectorMatrixProduct_result";
	rename -uid "2ABD8EA3-493A-8C0D-4C60-CCA25EC47D8B";
createNode mesh -n "vectorMatrixProduct_prVectorProduct_output_0Shape" -p "vectorMatrixProduct_prVectorProduct_output_0";
	rename -uid "B842F330-4318-8CB2-05AB-AD9682686D77";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39746848 0.39746848 -0.39746848 
		-0.39746848 0.39746848 -0.39746848 0.39746848 -0.5 -0.39746848 -0.39746848 -0.5 -0.39746848 
		0.39746848 -0.5 0.39746848 -0.39746848 -0.5 0.39746848 0.39746848 0.39746848 0.39746848 
		-0.39746848 0.39746848 0.39746848;
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
createNode transform -n "vectorMatrixProduct_prVectorProduct_output_2" -p "vectorMatrixProduct_result";
	rename -uid "CFF958DF-4CE1-C68B-B44E-9CA00A036B82";
createNode mesh -n "vectorMatrixProduct_prVectorProduct_output_2Shape" -p "vectorMatrixProduct_prVectorProduct_output_2";
	rename -uid "18F5774D-4A95-3700-5BEE-ACA94B97D13E";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.60253149 0.60253149 -0.39746851 
		-0.39746854 0.60253137 -0.60253149 0.39746851 -0.39746857 -0.39746848 -0.60253143 
		-0.39746842 -0.60253143 0.39746848 -0.5 0.60253149 -0.60253149 -0.5 0.39746848 0.60253143 
		0.5 0.60253143 -0.39746854 0.5 0.39746857;
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
createNode transform -n "pointMatrixProduct_result" -p "DONT_TOUCH";
	rename -uid "155C233B-4A0C-6A38-7E2A-06BDE8B336A3";
createNode transform -n "pointMatrixProduct_vectorProduct_output" -p "pointMatrixProduct_result";
	rename -uid "DE916677-405E-1AD8-8769-4F9801EC984D";
createNode mesh -n "pointMatrixProduct_vectorProduct_outputShape" -p "pointMatrixProduct_vectorProduct_output";
	rename -uid "5FD29027-44CD-6D9E-33F0-58BDC62FCBEB";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39099032 0.39099032 -0.39099032 
		-0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 -0.39099032 
		-0.39099032 -0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 
		0.39099032 0.39099032 0.39099032 0.39099032 -0.39099032 0.39099032 0.39099032;
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
createNode transform -n "pointMatrixProduct_prVectorProduct_output_0" -p "pointMatrixProduct_result";
	rename -uid "54B36CFF-4848-CC9E-4C8A-D98950D20CA1";
createNode mesh -n "pointMatrixProduct_prVectorProduct_output_0Shape" -p "pointMatrixProduct_prVectorProduct_output_0";
	rename -uid "89AECC89-4A21-7683-709B-45A3FBAA429F";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39746848 0.39746848 -0.39746848 
		-0.39746848 0.39746848 -0.39746848 0.39746848 -0.5 -0.39746848 -0.39746848 -0.5 -0.39746848 
		0.39746848 -0.5 0.39746848 -0.39746848 -0.5 0.39746848 0.39746848 0.39746848 0.39746848 
		-0.39746848 0.39746848 0.39746848;
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
createNode transform -n "pointMatrixProduct_prVectorProduct_output_2" -p "pointMatrixProduct_result";
	rename -uid "72AAB28C-4CCF-E5F5-F949-C8855237EEC6";
createNode mesh -n "pointMatrixProduct_prVectorProduct_output_2Shape" -p "pointMatrixProduct_prVectorProduct_output_2";
	rename -uid "4A97C81C-42BF-DEBD-DE64-75B16332BC7D";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.60253149 0.60253149 -0.39746851 
		-0.39746854 0.60253137 -0.60253149 0.39746851 -0.39746857 -0.39746848 -0.60253143 
		-0.39746842 -0.60253143 0.39746848 -0.5 0.60253149 -0.60253149 -0.5 0.39746848 0.60253143 
		0.5 0.60253143 -0.39746854 0.5 0.39746857;
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
createNode transform -n "input1_locator" -p "DONT_TOUCH";
	rename -uid "350F8BD8-4722-940B-C52C-07A63BF65D9E";
	setAttr ".v" no;
createNode locator -n "input1_locatorShape" -p "input1_locator";
	rename -uid "54456CFF-4592-DC32-6D55-3599132A0327";
	setAttr -k off ".v";
createNode transform -n "input2_locator" -p "DONT_TOUCH";
	rename -uid "467985BC-4A1F-CA4B-B6E9-6EB38818B029";
	setAttr ".v" no;
createNode locator -n "input2_locatorShape" -p "input2_locator";
	rename -uid "C9612A30-41DE-2BE8-B5B1-3EA7030C44A0";
	setAttr -k off ".v";
createNode transform -n "globalMatrix_locator" -p "DONT_TOUCH";
	rename -uid "E7A9A2CB-4A18-B4E1-8CCF-A0B7E4459A69";
	setAttr ".v" no;
createNode locator -n "globalMatrix_locatorShape" -p "globalMatrix_locator";
	rename -uid "D51FB7DC-4C64-85AB-E640-CF923ECED1C4";
	setAttr -k off ".v";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "67049068-40FB-00DD-DC57-DBB9AB272ACD";
	setAttr -s 7 ".lnk";
	setAttr -s 7 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "3055B4FF-4CE4-F957-7DEB-928D796A3FF7";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "80F58A28-4A17-D1DA-E95E-CCBAB805B5B2";
createNode displayLayerManager -n "layerManager";
	rename -uid "780B50D0-460D-64EA-283B-0F94E6EF2DAF";
createNode displayLayer -n "defaultLayer";
	rename -uid "8F93688F-46E3-F6B2-6739-A181975EFC16";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "162A4230-4B7D-B6DC-089C-93AAAF6CDA44";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "143B10B8-4219-D6B6-2030-EB8B52461AE1";
	setAttr ".g" yes;
createNode vectorProduct -n "noOperation_vectorProduct";
	rename -uid "D93B6729-4B46-0DF1-E461-DA9B8CF521D4";
	setAttr ".op" 0;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "26C7FD84-4F53-6297-3D65-EB96825D40BE";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode vectorProduct -n "dotProduct_vectorProduct";
	rename -uid "AEF3A760-489D-4449-3FBD-F9A04B2AABEA";
createNode vectorProduct -n "crossProduct_vectorProduct";
	rename -uid "D8DAF7D8-43E2-83E0-4308-69966B8D8480";
	setAttr ".op" 2;
createNode vectorProduct -n "vectorMatrixProduct_vectorProduct";
	rename -uid "6E16937E-4707-5F15-2D67-0099B6C80F3B";
	setAttr ".op" 3;
createNode vectorProduct -n "pointMatrixProduct_vectorProduct";
	rename -uid "A712C057-483F-3CE7-A6F2-1EA47F2D1F33";
	setAttr ".op" 4;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "E47736A6-4070-F555-53C5-DF9ED8D8FB8B";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -756.01570264738939 -707.19441251416072 ;
	setAttr ".tgi[0].vh" -type "double2" 1385.9150333834259 339.02175582021857 ;
	setAttr -s 12 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 461.04376220703125;
	setAttr ".tgi[0].ni[0].y" -86.695159912109375;
	setAttr ".tgi[0].ni[0].nvs" 18305;
	setAttr ".tgi[0].ni[1].x" 445.71533203125;
	setAttr ".tgi[0].ni[1].y" -282.60540771484375;
	setAttr ".tgi[0].ni[1].nvs" 18305;
	setAttr ".tgi[0].ni[2].x" 452.85818481445313;
	setAttr ".tgi[0].ni[2].y" -466.5670166015625;
	setAttr ".tgi[0].ni[2].nvs" 18305;
	setAttr ".tgi[0].ni[3].x" 453.13824462890625;
	setAttr ".tgi[0].ni[3].y" 46.801963806152344;
	setAttr ".tgi[0].ni[3].nvs" 18305;
	setAttr ".tgi[0].ni[4].x" 116.73699188232422;
	setAttr ".tgi[0].ni[4].y" -503.18045043945313;
	setAttr ".tgi[0].ni[4].nvs" 18305;
	setAttr ".tgi[0].ni[5].x" -379.42269897460938;
	setAttr ".tgi[0].ni[5].y" -106.10360717773438;
	setAttr ".tgi[0].ni[5].nvs" 18305;
	setAttr ".tgi[0].ni[6].x" -379.42269897460938;
	setAttr ".tgi[0].ni[6].y" -4.6750359535217285;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" 125.62889099121094;
	setAttr ".tgi[0].ni[7].y" -276.3280029296875;
	setAttr ".tgi[0].ni[7].nvs" 18305;
	setAttr ".tgi[0].ni[8].x" 136.21574401855469;
	setAttr ".tgi[0].ni[8].y" -68.353370666503906;
	setAttr ".tgi[0].ni[8].nvs" 18305;
	setAttr ".tgi[0].ni[9].x" 167.14285278320313;
	setAttr ".tgi[0].ni[9].y" 351.42855834960938;
	setAttr ".tgi[0].ni[9].nvs" 18306;
	setAttr ".tgi[0].ni[10].x" 127.52445983886719;
	setAttr ".tgi[0].ni[10].y" 119.12535858154297;
	setAttr ".tgi[0].ni[10].nvs" 18305;
	setAttr ".tgi[0].ni[11].x" 459.44155883789063;
	setAttr ".tgi[0].ni[11].y" 374.97390747070313;
	setAttr ".tgi[0].ni[11].nvs" 1923;
createNode lambert -n "noOperation_lambert";
	rename -uid "AF529FE9-4F8D-5D7A-DBC0-CA877E30475B";
	setAttr ".c" -type "float3" 1 0 0 ;
createNode shadingEngine -n "lambert2SG";
	rename -uid "450F9C43-4CD8-82CF-02A0-2A9D1B40D275";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
	rename -uid "2D6831B1-4905-24FF-BBAE-10A4F507F9D2";
createNode lambert -n "dotProduct_lambert";
	rename -uid "A0998577-4F0E-763D-54DB-A79402F8C5F9";
	setAttr ".c" -type "float3" 1 1 0 ;
createNode shadingEngine -n "lambert3SG";
	rename -uid "AED06F16-4D16-707A-E31D-0D8962A8A82B";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "1D4C4137-4314-4E31-CC3C-CEAD56E21F9C";
createNode lambert -n "crossProduct_lambert";
	rename -uid "53328FD6-405B-6EF7-770B-09898784371D";
	setAttr ".c" -type "float3" 0 1 0 ;
createNode shadingEngine -n "lambert4SG";
	rename -uid "5D52862A-43E4-7C9A-304C-57A54CC1BE9F";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo3";
	rename -uid "E2CE1209-4A7B-77A3-B68C-E9B2ECBA2986";
createNode lambert -n "vectorMatrixProduct_lambert";
	rename -uid "9B9F7AB5-47FB-D1F7-8804-68BF54210E0B";
	setAttr ".c" -type "float3" 0 1 1 ;
createNode shadingEngine -n "lambert5SG";
	rename -uid "09FCBAF2-4EE0-7173-344C-1F96F56742CF";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo4";
	rename -uid "00C94557-42A4-A796-77C4-F89209BDA6AC";
createNode lambert -n "pointMatrixProduct_lambert";
	rename -uid "F4C3756C-41B4-2F1B-0AC1-38A9886B7084";
	setAttr ".c" -type "float3" 0 0 1 ;
createNode shadingEngine -n "lambert6SG";
	rename -uid "B1B83C02-424F-56FE-3D82-E7807582AF1A";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo5";
	rename -uid "42CF9B4F-477D-F569-351A-E8A201CF9BEC";
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "C4DC043A-4021-69AF-A38C-B8A8DCE5802B";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -330.95236780151544 -323.80951094248991 ;
	setAttr ".tgi[0].vh" -type "double2" 317.85713022663526 338.09522466054096 ;
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
	setAttr -s 7 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 9 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "input1_locatorShape.wm" "input1_annotationShape.dom" -na;
connectAttr "input2_locatorShape.wm" "input2_annotationShape.dom" -na;
connectAttr "globalMatrix_locatorShape.wm" "globalMatrix_annotationShape.dom" -na
		;
connectAttr "noOperation_vectorProduct.o" "noOperation_vectorProduct_output.t";
connectAttr "dotProduct_vectorProduct.o" "dotProduct_vectorProduct_output.t";
connectAttr "crossProduct_vectorProduct.o" "crossProduct_vectorProduct_output.t"
		;
connectAttr "vectorMatrixProduct_vectorProduct.o" "vectorMatrixProduct_vectorProduct_output.t"
		;
connectAttr "pointMatrixProduct_vectorProduct.o" "pointMatrixProduct_vectorProduct_output.t"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert4SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert6SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert4SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert6SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "input2Shape.wp" "noOperation_vectorProduct.i2";
connectAttr "input1Shape.wp" "noOperation_vectorProduct.i1";
connectAttr "input2Shape.wm" "noOperation_vectorProduct.m";
connectAttr "input2Shape.wp" "dotProduct_vectorProduct.i2";
connectAttr "input1Shape.wp" "dotProduct_vectorProduct.i1";
connectAttr "input2Shape.wm" "dotProduct_vectorProduct.m";
connectAttr "input2Shape.wp" "crossProduct_vectorProduct.i2";
connectAttr "input1Shape.wp" "crossProduct_vectorProduct.i1";
connectAttr "input2Shape.wm" "crossProduct_vectorProduct.m";
connectAttr "input2Shape.wp" "vectorMatrixProduct_vectorProduct.i2";
connectAttr "input1Shape.wp" "vectorMatrixProduct_vectorProduct.i1";
connectAttr "input2Shape.wm" "vectorMatrixProduct_vectorProduct.m";
connectAttr "input2Shape.wp" "pointMatrixProduct_vectorProduct.i2";
connectAttr "input1Shape.wp" "pointMatrixProduct_vectorProduct.i1";
connectAttr "input2Shape.wm" "pointMatrixProduct_vectorProduct.m";
connectAttr "crossProduct_vectorProduct_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn"
		;
connectAttr "vectorMatrixProduct_vectorProduct_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "pointMatrixProduct_vectorProduct_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn"
		;
connectAttr "dotProduct_vectorProduct_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "pointMatrixProduct_vectorProduct.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn"
		;
connectAttr "input2Shape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn";
connectAttr "input1Shape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn";
connectAttr "vectorMatrixProduct_vectorProduct.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn"
		;
connectAttr "crossProduct_vectorProduct.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn"
		;
connectAttr "noOperation_vectorProduct.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn"
		;
connectAttr "dotProduct_vectorProduct.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn"
		;
connectAttr "noOperation_vectorProduct_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn"
		;
connectAttr "noOperation_lambert.oc" "lambert2SG.ss";
connectAttr "noOperation_prVectorProduct_output_2Shape.iog" "lambert2SG.dsm" -na
		;
connectAttr "noOperation_prVectorProduct_output_0Shape.iog" "lambert2SG.dsm" -na
		;
connectAttr "noOperation_vectorProduct_outputShape.iog" "lambert2SG.dsm" -na;
connectAttr "lambert2SG.msg" "materialInfo1.sg";
connectAttr "noOperation_lambert.msg" "materialInfo1.m";
connectAttr "dotProduct_lambert.oc" "lambert3SG.ss";
connectAttr "dotProduct_prVectorProduct_output_2Shape.iog" "lambert3SG.dsm" -na;
connectAttr "dotProduct_prVectorProduct_output_0Shape.iog" "lambert3SG.dsm" -na;
connectAttr "dotProduct_vectorProduct_outputShape.iog" "lambert3SG.dsm" -na;
connectAttr "lambert3SG.msg" "materialInfo2.sg";
connectAttr "dotProduct_lambert.msg" "materialInfo2.m";
connectAttr "crossProduct_lambert.oc" "lambert4SG.ss";
connectAttr "crossProduct_prVectorProduct_output_2Shape.iog" "lambert4SG.dsm" -na
		;
connectAttr "crossProduct_prVectorProduct_output_0Shape.iog" "lambert4SG.dsm" -na
		;
connectAttr "crossProduct_vectorProduct_outputShape.iog" "lambert4SG.dsm" -na;
connectAttr "lambert4SG.msg" "materialInfo3.sg";
connectAttr "crossProduct_lambert.msg" "materialInfo3.m";
connectAttr "vectorMatrixProduct_lambert.oc" "lambert5SG.ss";
connectAttr "vectorMatrixProduct_prVectorProduct_output_2Shape.iog" "lambert5SG.dsm"
		 -na;
connectAttr "vectorMatrixProduct_prVectorProduct_output_0Shape.iog" "lambert5SG.dsm"
		 -na;
connectAttr "vectorMatrixProduct_vectorProduct_outputShape.iog" "lambert5SG.dsm"
		 -na;
connectAttr "lambert5SG.msg" "materialInfo4.sg";
connectAttr "vectorMatrixProduct_lambert.msg" "materialInfo4.m";
connectAttr "pointMatrixProduct_lambert.oc" "lambert6SG.ss";
connectAttr "pointMatrixProduct_prVectorProduct_output_2Shape.iog" "lambert6SG.dsm"
		 -na;
connectAttr "pointMatrixProduct_prVectorProduct_output_0Shape.iog" "lambert6SG.dsm"
		 -na;
connectAttr "pointMatrixProduct_vectorProduct_outputShape.iog" "lambert6SG.dsm" 
		-na;
connectAttr "lambert6SG.msg" "materialInfo5.sg";
connectAttr "pointMatrixProduct_lambert.msg" "materialInfo5.m";
connectAttr "lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "lambert3SG.pa" ":renderPartition.st" -na;
connectAttr "lambert4SG.pa" ":renderPartition.st" -na;
connectAttr "lambert5SG.pa" ":renderPartition.st" -na;
connectAttr "lambert6SG.pa" ":renderPartition.st" -na;
connectAttr "noOperation_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "dotProduct_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "crossProduct_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "vectorMatrixProduct_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "pointMatrixProduct_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of test_prVectorProduct.ma
