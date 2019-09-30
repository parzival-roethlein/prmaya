//Maya ASCII 2018 scene
//Name: test_prVectorMath.ma
//Last modified: Mon, Sep 30, 2019 02:07:57 AM
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
	setAttr ".t" -type "double3" 0.79362335101431747 2.0409582213752708 3.5172304975187565 ;
	setAttr ".r" -type "double3" -21.938352729612575 8.6000000000001098 6.031354277005253e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "BCA98976-415B-B4E0-3363-7A8DC13AFFC9";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 4.1828608844472059;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 1.7071068286895752 1.1071068048477173 0 ;
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
	setAttr ".t" -type "double3" 1 0.4 0 ;
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
createNode transform -n "noOperation_prVectorMath_output_0" -p "noOperation_result";
	rename -uid "414A277B-4DD3-4F2A-1D11-6F82BA5F6B70";
	setAttr ".t" -type "double3" 0 1 0 ;
createNode mesh -n "noOperation_prVectorMath_output_0Shape" -p "noOperation_prVectorMath_output_0";
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
createNode transform -n "noOperation_prVectorMath_output_2" -p "noOperation_result";
	rename -uid "450411A6-446B-940D-003C-B397F0D77ED7";
	setAttr ".t" -type "double3" 0 1 0 ;
createNode mesh -n "noOperation_prVectorMath_output_2Shape" -p "noOperation_prVectorMath_output_2";
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
createNode transform -n "sum_result" -p "DONT_TOUCH";
	rename -uid "CFFD8756-40E8-F340-1087-E5ABD288B12C";
createNode transform -n "sum_vectorProduct_output" -p "sum_result";
	rename -uid "21B98532-4C14-7EF4-D891-4297111A78FA";
createNode mesh -n "sum_vectorProduct_outputShape" -p "sum_vectorProduct_output";
	rename -uid "31BE4E83-4C47-0301-1061-1E90846463E6";
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
createNode transform -n "sum_prVectorMath_output_0" -p "sum_result";
	rename -uid "F433FCF3-4BD3-E5F7-2E18-DA87EA0C27DB";
	setAttr ".t" -type "double3" 1 1.3999999761581421 0 ;
createNode mesh -n "sum_prVectorMath_output_0Shape" -p "sum_prVectorMath_output_0";
	rename -uid "479DEF6B-4D9E-5A0A-5A1F-59822CA528ED";
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
createNode transform -n "sum_prVectorMath_output_2" -p "sum_result";
	rename -uid "0BF84C03-450F-89EB-C8AC-8289B226A6EF";
	setAttr ".t" -type "double3" 1 1.3999999761581421 0 ;
createNode mesh -n "sum_prVectorMath_output_2Shape" -p "sum_prVectorMath_output_2";
	rename -uid "2F88A978-49D6-A0BC-8530-6A867140858F";
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
createNode transform -n "subtract_result" -p "DONT_TOUCH";
	rename -uid "FF71526C-4532-1C35-C2E5-1FA1D6765857";
createNode transform -n "subtract_vectorProduct_output" -p "subtract_result";
	rename -uid "0E622253-4986-3CCF-450B-0AB214A6D952";
createNode mesh -n "subtract_vectorProduct_outputShape" -p "subtract_vectorProduct_output";
	rename -uid "677A39E7-46E2-DE4B-D9DA-F180DAFF5DFE";
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
createNode transform -n "subtract_prVectorMath_output_0" -p "subtract_result";
	rename -uid "A853BCF7-4AEF-D7DB-E378-CD880251EBC3";
	setAttr ".t" -type "double3" -1 0.60000002384185791 0 ;
createNode mesh -n "subtract_prVectorMath_output_0Shape" -p "subtract_prVectorMath_output_0";
	rename -uid "9EC9E0D5-44E2-F419-A7FC-FA8E4857DECC";
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
createNode transform -n "subtract_prVectorMath_output_2" -p "subtract_result";
	rename -uid "1EF55B28-49C3-EC57-2B47-A59342364DBC";
	setAttr ".t" -type "double3" -1 0.60000002384185791 0 ;
createNode mesh -n "subtract_prVectorMath_output_2Shape" -p "subtract_prVectorMath_output_2";
	rename -uid "9895B431-4D42-B558-AE78-EE882D581C7C";
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
createNode transform -n "average_result" -p "DONT_TOUCH";
	rename -uid "06C85A68-45FA-360E-396B-80BD41A1143E";
createNode transform -n "average_vectorProduct_output" -p "average_result";
	rename -uid "20BDDC42-44D3-E762-BD1A-EDB5B319D944";
createNode mesh -n "average_vectorProduct_outputShape" -p "average_vectorProduct_output";
	rename -uid "512D98D3-4E37-7499-D295-F98E53B490D5";
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
createNode transform -n "average_prVectorMath_output_0" -p "average_result";
	rename -uid "E239FDB7-4C33-D7BC-527A-5FAAA2A8F5B3";
	setAttr ".t" -type "double3" 0.5 0.69999998807907104 0 ;
createNode mesh -n "average_prVectorMath_output_0Shape" -p "average_prVectorMath_output_0";
	rename -uid "6B1AB520-4949-4560-6E84-5EBF3497F172";
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
createNode transform -n "average_prVectorMath_output_2" -p "average_result";
	rename -uid "08A37C7F-42A9-2F08-E8FA-B0977703EB97";
	setAttr ".t" -type "double3" 0.5 0.69999998807907104 0 ;
createNode mesh -n "average_prVectorMath_output_2Shape" -p "average_prVectorMath_output_2";
	rename -uid "5758A00A-4757-8D80-8D4F-E5A6E1D5AD0D";
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
createNode transform -n "dotProduct_prVectorMath_output_0" -p "dotProduct_result";
	rename -uid "147D6430-4108-2E4A-38C7-4786DD152C5F";
	setAttr ".t" -type "double3" 0.40000000596046448 0.40000000596046448 0.40000000596046448 ;
createNode mesh -n "dotProduct_prVectorMath_output_0Shape" -p "dotProduct_prVectorMath_output_0";
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
createNode transform -n "dotProduct_prVectorMath_output_2" -p "dotProduct_result";
	rename -uid "3C288495-4C31-ACFD-3B15-1DA7AD83C496";
	setAttr ".t" -type "double3" 0.40000000596046448 0.40000000596046448 0.40000000596046448 ;
createNode mesh -n "dotProduct_prVectorMath_output_2Shape" -p "dotProduct_prVectorMath_output_2";
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
createNode transform -n "crossProduct_prVectorMath_output_0" -p "crossProduct_result";
	rename -uid "4317B2C4-4832-357B-19AE-4B837158C810";
	setAttr ".t" -type "double3" 0 0 -1 ;
createNode mesh -n "crossProduct_prVectorMath_output_0Shape" -p "crossProduct_prVectorMath_output_0";
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
createNode transform -n "crossProduct_prVectorMath_output_2" -p "crossProduct_result";
	rename -uid "48A33855-4CEF-8A20-3F41-E1B550B06F9D";
	setAttr ".t" -type "double3" 0 0 -1 ;
createNode mesh -n "crossProduct_prVectorMath_output_2Shape" -p "crossProduct_prVectorMath_output_2";
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
createNode transform -n "vectorMatrixProduct_prVectorMath_output_0" -p "vectorMatrixProduct_result";
	rename -uid "2ABD8EA3-493A-8C0D-4C60-CCA25EC47D8B";
	setAttr ".t" -type "double3" 0.70710676908493042 0.70710676908493042 0 ;
createNode mesh -n "vectorMatrixProduct_prVectorMath_output_0Shape" -p "vectorMatrixProduct_prVectorMath_output_0";
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
createNode transform -n "vectorMatrixProduct_prVectorMath_output_2" -p "vectorMatrixProduct_result";
	rename -uid "CFF958DF-4CE1-C68B-B44E-9CA00A036B82";
	setAttr ".t" -type "double3" 0.70710676908493042 0.70710676908493042 0 ;
createNode mesh -n "vectorMatrixProduct_prVectorMath_output_2Shape" -p "vectorMatrixProduct_prVectorMath_output_2";
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
createNode transform -n "pointMatrixProduct_prVectorMath_output_0" -p "pointMatrixProduct_result";
	rename -uid "54B36CFF-4848-CC9E-4C8A-D98950D20CA1";
	setAttr ".t" -type "double3" 1.7071068286895752 1.1071068048477173 0 ;
createNode mesh -n "pointMatrixProduct_prVectorMath_output_0Shape" -p "pointMatrixProduct_prVectorMath_output_0";
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
createNode transform -n "pointMatrixProduct_prVectorMath_output_2" -p "pointMatrixProduct_result";
	rename -uid "72AAB28C-4CCF-E5F5-F949-C8855237EEC6";
	setAttr ".t" -type "double3" 1.7071068286895752 1.1071068048477173 0 ;
createNode mesh -n "pointMatrixProduct_prVectorMath_output_2Shape" -p "pointMatrixProduct_prVectorMath_output_2";
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
createNode transform -n "project_in1_on_in2_result" -p "DONT_TOUCH";
	rename -uid "42C007C4-42A0-E332-AC97-B6B8B8FA2A5C";
createNode transform -n "project_in1_on_in2_prVectorMath_output_0" -p "project_in1_on_in2_result";
	rename -uid "9C61EBEE-476F-3BD6-D9E6-D389DC9C2476";
	setAttr ".t" -type "double3" 0.34482759237289429 0.13793103396892548 0 ;
createNode mesh -n "project_in1_on_in2_prVectorMath_output_0Shape" -p "project_in1_on_in2_prVectorMath_output_0";
	rename -uid "809F1124-49A1-AD04-ECFD-F5B102CD6B2E";
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
		-0.39746848 0.39746848 -0.39746848 0.39746848 -0.49999994 -0.39746848 -0.39746848 
		-0.50000006 -0.39746848 0.39746848 -0.49999994 0.39746848 -0.39746848 -0.50000006 
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
createNode transform -n "project_in1_on_in2_prVectorMath_output_2" -p "project_in1_on_in2_result";
	rename -uid "A5B3BF7E-402D-7F7E-9E8E-AE9BCC31DADD";
	setAttr ".t" -type "double3" 0.34482759237289429 0.13793103396892548 0 ;
createNode mesh -n "project_in1_on_in2_prVectorMath_output_2Shape" -p "project_in1_on_in2_prVectorMath_output_2";
	rename -uid "8FD0BDE1-4454-F0AB-4814-42B5178BDCE2";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39746848 0.5 -0.39746848 
		-0.39746848 0.5 -0.39746848 0.39746848 -0.39746842 -0.39746848 -0.39746848 -0.39746851 
		-0.39746848 0.39746848 -0.39746842 0.39746848 -0.39746848 -0.39746851 0.39746848 
		0.39746848 0.5 0.39746848 -0.39746848 0.5 0.39746848;
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
createNode transform -n "project_in2_on_in1_result" -p "DONT_TOUCH";
	rename -uid "8D89C700-4C1D-4498-F1D4-44A0059BA84D";
createNode transform -n "project_in2_on_in1_prVectorMath_output_0" -p "project_in2_on_in1_result";
	rename -uid "E9BCA3F9-40E0-7DC6-FF84-65A219895622";
	setAttr ".t" -type "double3" 0 0.40000000596046448 0 ;
createNode mesh -n "project_in2_on_in1_prVectorMath_output_0Shape" -p "project_in2_on_in1_prVectorMath_output_0";
	rename -uid "8503B59A-41E1-45FC-90ED-42824CCB5047";
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
		-0.39746848 0.39746848 -0.39746848 0.39746848 -0.49999994 -0.39746848 -0.39746848 
		-0.50000006 -0.39746848 0.39746848 -0.49999994 0.39746848 -0.39746848 -0.50000006 
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
createNode transform -n "project_in2_on_in1_prVectorMath_output_2" -p "project_in2_on_in1_result";
	rename -uid "B6AC31FA-4C5F-AA80-78D4-D985A7D87D57";
	setAttr ".t" -type "double3" 0 0.40000000596046448 0 ;
createNode mesh -n "project_in2_on_in1_prVectorMath_output_2Shape" -p "project_in2_on_in1_prVectorMath_output_2";
	rename -uid "59CD450B-40D0-6111-DDFC-C29C07BAFF62";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39746848 0.5 -0.39746848 
		-0.39746848 0.5 -0.39746848 0.39746848 -0.39746842 -0.39746848 -0.39746848 -0.39746851 
		-0.39746848 0.39746848 -0.39746842 0.39746848 -0.39746848 -0.39746851 0.39746848 
		0.39746848 0.5 0.39746848 -0.39746848 0.5 0.39746848;
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
	rename -uid "FC658F4D-474E-2534-1810-4D9B26A72CF7";
	setAttr -s 11 ".lnk";
	setAttr -s 11 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "5B72DB24-4A53-5E38-1A2A-B1B28D9A19C6";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "B07F1197-42E7-3BC0-4126-708530382A5C";
createNode displayLayerManager -n "layerManager";
	rename -uid "024DC7AF-41D6-CCD6-6BB9-649935DD6F87";
createNode displayLayer -n "defaultLayer";
	rename -uid "8F93688F-46E3-F6B2-6739-A181975EFC16";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "33C50582-4B17-F7A7-128F-E0902984E46A";
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
	setAttr ".op" 5;
createNode vectorProduct -n "vectorMatrixProduct_vectorProduct";
	rename -uid "6E16937E-4707-5F15-2D67-0099B6C80F3B";
	setAttr ".op" 3;
createNode vectorProduct -n "pointMatrixProduct_vectorProduct";
	rename -uid "A712C057-483F-3CE7-A6F2-1EA47F2D1F33";
	setAttr ".op" 4;
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
createNode lambert -n "project_lambert";
	rename -uid "D514EFD4-448F-494B-43E0-D79107E47FA4";
	setAttr ".c" -type "float3" 1 0 1 ;
createNode shadingEngine -n "lambert7SG";
	rename -uid "FA26C06A-49B4-29C3-D8F5-47A5CE6E48F4";
	setAttr ".ihi" 0;
	setAttr -s 4 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo6";
	rename -uid "6B9839AB-4E8C-6632-840F-1B840C5BC0F4";
createNode plusMinusAverage -n "plusMinusAverage1";
	rename -uid "92624152-482E-ECB5-CA0D-86A06FD20E9C";
createNode lambert -n "sum_lambert";
	rename -uid "87A26ED2-4049-B074-9FCC-058780BC8027";
	setAttr ".c" -type "float3" 1 1 1 ;
createNode shadingEngine -n "lambert8SG";
	rename -uid "125A2F68-4BF6-7534-D8E4-2C8E14E8BF6C";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo7";
	rename -uid "BE48DF37-4E4C-8393-9D93-19A0CF50DAC6";
createNode lambert -n "subtract_lambert";
	rename -uid "7193A74E-490B-B32F-CEF5-ECBB80C04F04";
createNode shadingEngine -n "lambert9SG";
	rename -uid "8A7197A8-4CCC-FA01-DACB-D981D6B709BF";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo8";
	rename -uid "5C20DFB3-4A32-E63C-CD03-D18AD342E7D6";
createNode lambert -n "average_lambert";
	rename -uid "2F6741C0-4C16-3AC3-B133-54B5471F177B";
	setAttr ".c" -type "float3" 0.042168677 0.042168677 0.042168677 ;
createNode shadingEngine -n "lambert10SG";
	rename -uid "4D4C3C82-4DBB-53B3-DFCB-9AA6DDA6D2E9";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo9";
	rename -uid "53F239E2-42CA-7D0B-1332-E5A0BD83A452";
createNode plusMinusAverage -n "sum_plusMinusAverage";
	rename -uid "17DAA166-42A9-3DEC-BBC6-6EA488B8AE80";
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "subtract_plusMinusAverage";
	rename -uid "61C6E7C3-4AEF-4C8F-0A14-3E898A959A5B";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "average_plusMinusAverage";
	rename -uid "BDA36DC7-4B49-7551-2F1B-B38222E0145B";
	setAttr ".op" 3;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "BEB6378F-4F61-FD61-B1A4-88B54080AFA2";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -1399.7210917038294 -660.27325745938117 ;
	setAttr ".tgi[0].vh" -type "double2" 877.70828105338467 452.12659372980414 ;
	setAttr -s 8 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -627.95977783203125;
	setAttr ".tgi[0].ni[0].y" -495.51055908203125;
	setAttr ".tgi[0].ni[0].nvs" 18305;
	setAttr ".tgi[0].ni[1].x" -1252.857177734375;
	setAttr ".tgi[0].ni[1].y" 94.285713195800781;
	setAttr ".tgi[0].ni[1].nvs" 18305;
	setAttr ".tgi[0].ni[2].x" -1252.857177734375;
	setAttr ".tgi[0].ni[2].y" -60;
	setAttr ".tgi[0].ni[2].nvs" 18305;
	setAttr ".tgi[0].ni[3].x" -908.63427734375;
	setAttr ".tgi[0].ni[3].y" 152.75129699707031;
	setAttr ".tgi[0].ni[3].nvs" 18305;
	setAttr ".tgi[0].ni[4].x" -540.0770263671875;
	setAttr ".tgi[0].ni[4].y" 19.354642868041992;
	setAttr ".tgi[0].ni[4].nvs" 18305;
	setAttr ".tgi[0].ni[5].x" -944.51812744140625;
	setAttr ".tgi[0].ni[5].y" -373.42962646484375;
	setAttr ".tgi[0].ni[5].nvs" 18305;
	setAttr ".tgi[0].ni[6].x" -522.1064453125;
	setAttr ".tgi[0].ni[6].y" 347.01632690429688;
	setAttr ".tgi[0].ni[6].nvs" 18305;
	setAttr ".tgi[0].ni[7].x" -911.02655029296875;
	setAttr ".tgi[0].ni[7].y" -119.73451232910156;
	setAttr ".tgi[0].ni[7].nvs" 18305;
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
	setAttr -s 11 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 13 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 3 ".u";
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
connectAttr "sum_plusMinusAverage.o3" "sum_vectorProduct_output.t";
connectAttr "subtract_plusMinusAverage.o3" "subtract_vectorProduct_output.t";
connectAttr "average_plusMinusAverage.o3" "average_vectorProduct_output.t";
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
relationship "link" ":lightLinker1" "lambert7SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert8SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert9SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert10SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert4SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert6SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert7SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert8SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert9SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert10SG.message" ":defaultLightSet.message";
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
connectAttr "noOperation_lambert.oc" "lambert2SG.ss";
connectAttr "noOperation_prVectorMath_output_2Shape.iog" "lambert2SG.dsm" -na;
connectAttr "noOperation_prVectorMath_output_0Shape.iog" "lambert2SG.dsm" -na;
connectAttr "noOperation_vectorProduct_outputShape.iog" "lambert2SG.dsm" -na;
connectAttr "lambert2SG.msg" "materialInfo1.sg";
connectAttr "noOperation_lambert.msg" "materialInfo1.m";
connectAttr "dotProduct_lambert.oc" "lambert3SG.ss";
connectAttr "dotProduct_prVectorMath_output_2Shape.iog" "lambert3SG.dsm" -na;
connectAttr "dotProduct_prVectorMath_output_0Shape.iog" "lambert3SG.dsm" -na;
connectAttr "dotProduct_vectorProduct_outputShape.iog" "lambert3SG.dsm" -na;
connectAttr "lambert3SG.msg" "materialInfo2.sg";
connectAttr "dotProduct_lambert.msg" "materialInfo2.m";
connectAttr "crossProduct_lambert.oc" "lambert4SG.ss";
connectAttr "crossProduct_prVectorMath_output_2Shape.iog" "lambert4SG.dsm" -na;
connectAttr "crossProduct_prVectorMath_output_0Shape.iog" "lambert4SG.dsm" -na;
connectAttr "crossProduct_vectorProduct_outputShape.iog" "lambert4SG.dsm" -na;
connectAttr "lambert4SG.msg" "materialInfo3.sg";
connectAttr "crossProduct_lambert.msg" "materialInfo3.m";
connectAttr "vectorMatrixProduct_lambert.oc" "lambert5SG.ss";
connectAttr "vectorMatrixProduct_prVectorMath_output_2Shape.iog" "lambert5SG.dsm"
		 -na;
connectAttr "vectorMatrixProduct_prVectorMath_output_0Shape.iog" "lambert5SG.dsm"
		 -na;
connectAttr "vectorMatrixProduct_vectorProduct_outputShape.iog" "lambert5SG.dsm"
		 -na;
connectAttr "lambert5SG.msg" "materialInfo4.sg";
connectAttr "vectorMatrixProduct_lambert.msg" "materialInfo4.m";
connectAttr "pointMatrixProduct_lambert.oc" "lambert6SG.ss";
connectAttr "pointMatrixProduct_prVectorMath_output_2Shape.iog" "lambert6SG.dsm"
		 -na;
connectAttr "pointMatrixProduct_prVectorMath_output_0Shape.iog" "lambert6SG.dsm"
		 -na;
connectAttr "pointMatrixProduct_vectorProduct_outputShape.iog" "lambert6SG.dsm" 
		-na;
connectAttr "lambert6SG.msg" "materialInfo5.sg";
connectAttr "pointMatrixProduct_lambert.msg" "materialInfo5.m";
connectAttr "project_lambert.oc" "lambert7SG.ss";
connectAttr "project_in2_on_in1_prVectorMath_output_2Shape.iog" "lambert7SG.dsm"
		 -na;
connectAttr "project_in2_on_in1_prVectorMath_output_0Shape.iog" "lambert7SG.dsm"
		 -na;
connectAttr "project_in1_on_in2_prVectorMath_output_2Shape.iog" "lambert7SG.dsm"
		 -na;
connectAttr "project_in1_on_in2_prVectorMath_output_0Shape.iog" "lambert7SG.dsm"
		 -na;
connectAttr "lambert7SG.msg" "materialInfo6.sg";
connectAttr "project_lambert.msg" "materialInfo6.m";
connectAttr "sum_lambert.oc" "lambert8SG.ss";
connectAttr "sum_prVectorMath_output_2Shape.iog" "lambert8SG.dsm" -na;
connectAttr "sum_prVectorMath_output_0Shape.iog" "lambert8SG.dsm" -na;
connectAttr "sum_vectorProduct_outputShape.iog" "lambert8SG.dsm" -na;
connectAttr "lambert8SG.msg" "materialInfo7.sg";
connectAttr "sum_lambert.msg" "materialInfo7.m";
connectAttr "subtract_lambert.oc" "lambert9SG.ss";
connectAttr "subtract_prVectorMath_output_2Shape.iog" "lambert9SG.dsm" -na;
connectAttr "subtract_prVectorMath_output_0Shape.iog" "lambert9SG.dsm" -na;
connectAttr "subtract_vectorProduct_outputShape.iog" "lambert9SG.dsm" -na;
connectAttr "lambert9SG.msg" "materialInfo8.sg";
connectAttr "subtract_lambert.msg" "materialInfo8.m";
connectAttr "average_lambert.oc" "lambert10SG.ss";
connectAttr "average_prVectorMath_output_2Shape.iog" "lambert10SG.dsm" -na;
connectAttr "average_prVectorMath_output_0Shape.iog" "lambert10SG.dsm" -na;
connectAttr "average_vectorProduct_outputShape.iog" "lambert10SG.dsm" -na;
connectAttr "lambert10SG.msg" "materialInfo9.sg";
connectAttr "average_lambert.msg" "materialInfo9.m";
connectAttr "input1.t" "sum_plusMinusAverage.i3[0]";
connectAttr "input2.t" "sum_plusMinusAverage.i3[1]";
connectAttr "input1.t" "subtract_plusMinusAverage.i3[0]";
connectAttr "input2.t" "subtract_plusMinusAverage.i3[1]";
connectAttr "input1.t" "average_plusMinusAverage.i3[0]";
connectAttr "input2.t" "average_plusMinusAverage.i3[1]";
connectAttr "average_vectorProduct_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn"
		;
connectAttr "input2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "input1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "sum_plusMinusAverage.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "subtract_vectorProduct_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn"
		;
connectAttr "average_plusMinusAverage.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr "sum_vectorProduct_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn"
		;
connectAttr "subtract_plusMinusAverage.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn"
		;
connectAttr "lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "lambert3SG.pa" ":renderPartition.st" -na;
connectAttr "lambert4SG.pa" ":renderPartition.st" -na;
connectAttr "lambert5SG.pa" ":renderPartition.st" -na;
connectAttr "lambert6SG.pa" ":renderPartition.st" -na;
connectAttr "lambert7SG.pa" ":renderPartition.st" -na;
connectAttr "lambert8SG.pa" ":renderPartition.st" -na;
connectAttr "lambert9SG.pa" ":renderPartition.st" -na;
connectAttr "lambert10SG.pa" ":renderPartition.st" -na;
connectAttr "noOperation_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "dotProduct_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "crossProduct_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "vectorMatrixProduct_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "pointMatrixProduct_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "project_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "sum_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "subtract_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "average_lambert.msg" ":defaultShaderList1.s" -na;
connectAttr "sum_plusMinusAverage.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "subtract_plusMinusAverage.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "average_plusMinusAverage.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of test_prVectorMath.ma
